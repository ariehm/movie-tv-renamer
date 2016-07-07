import os
import sys
import subprocess
import datetime
import shutil

import files
import renamers
import cleaneruppers
import contentfinders

def main(
	homeDir, 
	handledContentFilePath, 
	logFilePath, 
	completeDir, 
	backupRoot, 
	excludeDirs, 
	extensions,
	maxLogEntries,
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

if __name__ == "__main__":
	fileManagementImpl = "SymLinks"
	homeDir = "/Users/rdelhommer"
	handledContentFilePath = homeDir + "/media-manager/handled-content"
	logFilePath = homeDir + "/media-manager/auto-media-manager.log"
	completeDir = homeDir + "/media"
	backupRoot = homeDir + "/backup"
	excludeDirs = [completeDir + '/incomplete']
	extensions = ['.mkv', '.mp4', '.ts']
	maxLogEntries = 1000
	ratioThreshold = 1.25

	renamer = None
	cleanerUpper = None

	if FileManagementImpl == "SymLinks":
		renamer = renamers.SymLinkRenamer(backupRoot)
		cleanerUpper = cleaneruppers.SymLinkCleanerUpper(backupRoot)
	else:
		renamer = renamers.CopyRenamer(backupRoot)
		cleanerUpper = cleaneruppers.CopyCleanerUpper(backupRoot)

	main( 
		homeDir, 
		handledContentFilePath, 
		logFilePath, 
		completeDir, 
		backupRoot, 
		excludeDirs, 
		extensions,
		maxLogEntries,
		ratioThreshold,
		renamer,
		cleanerUpper)




