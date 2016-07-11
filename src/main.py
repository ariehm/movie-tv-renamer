import os
import sys
import getopt

import files
import renamers
import cleaneruppers
import contentfinders
import config

def main(
	completeDir, 
	backupRoot, 
	excludeDirs, 
	extensions,
	ratioThreshold,
	renamer,
	cleanerUpper):

	contentFinder = contentfinders.ContentFinder(completeDir)
	completeContentPaths = contentFinder.getCompleteContentFilePaths(
		excludeDirs, extensions)

	completeMediaFiles = [files.MediaFile(f) for f in completeContentPaths]

	# rename unhandled files
	for file in mediaFilesToHandle:
		renamer.renameFile(file)

	cleanerUpper(completeContentPaths, ratioThreshold).clean()

def getOptions(argv):
	configFilePath = ''

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'main.py -c <configfile>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print 'main.py -c <configfile>'
			sys.exit()
		elif opt in ("-c", "--cfile"):
			configFilePath = arg

	return {'c': configFilePath}

def getConfigs(configFilePath):
	# return default config if none specified
	if configFilePath == '':
		return config.Config()

	return config.ConfigSerializer().deserializeConfig(configFilePath)

if __name__ == "__main__":
	options = getOptions(sys.argv[1:])
	config = getConfigs(options['c'])

	renamer = None
	cleanerUpper = None

	if config.fileManagement == "SymLinks":
		renamer = renamers.SymLinkRenamer(config.backupRoot)
		cleanerUpper = cleaneruppers.SymLinkCleanerUpper(config.backupRoot)
	else:
		renamer = renamers.CopyRenamer(config.backupRoot)
		cleanerUpper = cleaneruppers.CopyCleanerUpper(config.backupRoot)

	main( 
		config.completeDir, 
		config.backupRoot, 
		config.excludeDirs, 
		config.extensions,
		config.ratioThreshold,
		renamer,
		cleanerUpper)




