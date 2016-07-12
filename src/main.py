import os
import sys
import getopt

import files
import renamers
import mrclean
from contentfinders import ContentFinder
import config
import jsonserializer

def getOptions(argv):
    print argv
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
    renamer = None
    mrcleans = []

    if config.client == 'transmission':
        transmissionMrClean = mrclean.MrClean(
            mrclean.TransmissionCleanExecutor(),
            mrclean.TransmissionCleanTrigger(config.ratioThreshold))

        mrcleans.append(transmissionMrClean)

    if config.fileManagement == 'symlinks':
        renamer = renamers.SymLinkRenamer(config.backupRoot)
        mrcleans.append(mrclean.MrClean(mrclean.SymLinkCleanExecutor(config.backupRoot)))
    else:
        renamer = renamers.CopyRenamer(config.backupRoot)
        mrcleans.append(mrclean.MrClean(mrclean.CopyCleanExecutor()))

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

    completeContentPaths = ContentFinder.getCompleteContentFilePaths(
        completeDir, excludeDirs, extensions)

    completeMediaFiles = [files.MediaFile(f) for f in completeContentPaths]

    # rename unhandled files
    for file in mediaFilesToHandle:
        renamer.renameFile(file)

    # clean up
    for mrClean in mrCleans:
        mrClean.clean(completeContentPaths)

if __name__ == "__main__":
    options = getOptions(sys.argv[1:])
    print(options)
    config = getConfigs(options['c'])
    dependencies = getDependencies(config)

    runManager( 
        config.completeDir, 
        config.excludeDirs, 
        config.extensions,
        dependencies['renamer'],
        dependencies['mrcleans'])




