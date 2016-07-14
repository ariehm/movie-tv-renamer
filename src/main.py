import os
import sys
import getopt
import logging
from logging.handlers import RotatingFileHandler

import files
import renamers
import mrclean
from contentfinders import ContentFinder
import config
import jsonserializer
import nameparsers
import media

def getOptions(argv):
    configFilePath = ''

    try:
        opts, args = getopt.getopt(argv,"hc:",["cfile="])
    except getopt.GetoptError:
        print 'CMD ARGS ERROR: main.py -c <configfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'HELP: main.py -c <configfile>'
            sys.exit()
        elif opt in ("-c", "--cfile"):
            configFilePath = arg

    return {'c': configFilePath}

def getConfigs(configFilePath):
    # return default config if none specified
    if not os.path.exists(configFilePath) or configFilePath == '':
        return config.Config.getDefaultConfig()

    return config.Config.loadFromFile(jsonserializer.JsonSerializer(), configFilePath)

def getDependencies(config):
    log = logging.getLogger('root')
    renamer = None
    mrcleans = []

    if config.client == 'transmission':
        log.info('Setting up Transmission MrClean')
        transmissionMrClean = mrclean.MrClean(
            mrclean.TransmissionCleanExecutor(),
            mrclean.TransmissionCleanTrigger(config.ratioThreshold))

        mrcleans.append(transmissionMrClean)

    if config.fileManagement == 'symlink':
        log.info('Setting up SYMLINKS file management')
        renamer = renamers.SymLinkRenamer(config.backupRoot)
        symlinkMrClean = mrclean.MrClean(
            mrclean.SymLinkCleanExecutor(config.backupRoot),
            mrclean.TransmissionCleanTrigger(config.ratioThreshold))

        mrcleans.append(symlinkMrClean)
    else:
        log.info('Setting up COPY file management')
        renamer = renamers.CopyRenamer(config.backupRoot)
        copyMrClean = mrclean.MrClean(
            mrclean.CopyCleanExecutor(),
            mrclean.TransmissionCleanTrigger(config.ratioThreshold))

        mrcleans.append(copyMrClean)

    dependencies = {}
    dependencies['renamer'] = renamer
    dependencies['mrcleans'] = mrcleans

    return dependencies


def runManager(
    completeDir,
    excludeDirs, 
    extensions,
    ratioThreshold,
    renamer,
    mrCleans):
    log = logging.getLogger('root')

    completeContentPaths = ContentFinder.getCompleteContentFilePaths(
        completeDir, excludeDirs, extensions)

    mediaFileFactory = files.MediaFileFactory()
    nameParserFactory = nameparsers.NameParserFactory()
    mediaFactory = media.MediaFactory()

    completeMediaFiles = []
    for f in completeContentPaths:
        mediaFile = mediaFileFactory.buildMediaFile(f, nameParserFactory, mediaFactory)

        if mediaFile:
            completeMediaFiles.append(mediaFile)

    # rename unhandled files
    for file in completeMediaFiles:
        renamer.renameFile(file)

    # clean up
    for mrClean in mrCleans:
        mrClean.clean(completeContentPaths)

if __name__ == "__main__":
    logFormatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')

    logFile = 'media-tv-renamer.log'

    logHandler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)
    logHandler.setFormatter(logFormatter)
    logHandler.setLevel(logging.INFO)

    log = logging.getLogger('root')
    log.setLevel(logging.INFO)

    log.addHandler(logHandler)

    log.info('Renamer Started')

    options = getOptions(sys.argv[1:])

    config = getConfigs(options['c'])

    dependencies = getDependencies(config)

    runManager( 
        config.completeDir, 
        config.excludeDirs, 
        config.extensions,
        config.ratioThreshold,
        dependencies['renamer'],
        dependencies['mrcleans'])

    log.info('Renamer Finished')




