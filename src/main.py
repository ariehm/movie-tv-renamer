import os
import sys
import subprocess
import datetime
import shutil

import files
import renamers
import cleaneruppers
import contentfinders

# todo:
# dont use handled-content file.  just check all files.  if the renamed symlink/file exists, then do nothing for that file
# remove seed after ratio is over threshold (1.25?)
# add logging

def main(
	fileManagementImpl, 
	homeDir, 
	handledContentFilePath, 
	logFilePath, 
	completeDir, 
	backupRoot, 
	excludeDirs, 
	extensions,
	maxLogEntries,
	ratioThreshold):

	contentFinder = contentfinders.ContentFinder(completeDir)
	completeContentPaths = contentFinder.getCompleteContentFilePaths(
		excludeDirs, extensions)

	# get videos that are in complete directory but have not been handled yet
	mediaFilesToHandle = [files.MediaFile(f) for f in completeContentPaths]

	# exit if there is nothing new to handle
	if len(mediaFilesToHandle) is 0:
		print("none to handle")
		sys.exit()

	if FileManagementImpl == "SymLinks":
		renamer = renamers.SymLinkRenamer(backupRoot)
	else:
		renamer = renamers.CopyRenamer(backupRoot)

	# rename unhandled files
	for file in mediaFilesToHandle:
		if renamer.renameFile(file):
			handledContentFile.addHandledFilePath(file.fullName)

	if FileManagementImpl == "SymLinks":
		renamer = cleaneruppers.SymLinkCleanerUpper(backupRoot)
	else:
		renamer = cleaneruppers.CopyCleanerUpper(backupRoot)

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

	main(
		fileManagementImpl, 
		homeDir, 
		handledContentFilePath, 
		logFilePath, 
		completeDir, 
		backupRoot, 
		excludeDirs, 
		extensions,
		maxLogEntries,
		ratioThreshold)




