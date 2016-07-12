import json
import os

class Config:
	FILE_MANAGEMENT_KEY = 'file-management'
	COMPLETE_DIR_KEY = 'complete-dir'
	BACKUP_ROOT_KEY = 'backup-root'
	EXCLUDE_DIRS_KEY = 'exclude-dirs'
	EXTENSIONS_KEY = 'extensions'
	RATIO_THRESHOLD_KEY = 'ratio-threshold'

	FILE_MANAGEMENT_DEFAULT = 'symlinks'
	COMPLETE_DIR_DEFAULT = 'complete'
	BACKUP_ROOT_DEFAULT = 'backup'
	EXCLUDE_DIRS_DEFAULT = []
	EXTENSIONS_DEFAULT = ['.mkv', '.mp4', '.ts', '.mov', '.avi']
	RATIO_THRESHOLD_DEFAULT = 2

	@staticmethod
	def loadFromFile(serializer, filePath):
		deserializedDict = serializer.deserializeFromFile(filePath)

		fileManagement = Config.FILE_MANAGEMENT_DEFAULT
		completeDir = Config.COMPLETE_DIR_DEFAULT
		backupRoot = Config.BACKUP_ROOT_DEFAULT
		excludeDirs = Config.EXCLUDE_DIRS_DEFAULT
		extensions = Config.EXTENSIONS_DEFAULT
		ratioThreshold = Config.RATIO_THRESHOLD_DEFAULT

		if Config.FILE_MANAGEMENT_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.FILE_MANAGEMENT_KEY]
		if Config.COMPLETE_DIR_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.COMPLETE_DIR_KEY]
		if Config.BACKUP_ROOT_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.BACKUP_ROOT_KEY]
		if Config.EXCLUDE_DIRS_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.EXCLUDE_DIRS_KEY]
		if Config.EXTENSIONS_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.EXTENSIONS_KEY]
		if Config.RATIO_THRESHOLD_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.RATIO_THRESHOLD_KEY]

		return Config(
			fileManagement,
			completeDir,
			backupRoot,
			excludeDirs,
			extensions,
			ratioThreshold)

	def saveToFile(self, serializer, filePath):
		serializer.serializeToFile(self, filePath)

	def __init__(
		self,
		fileManagement,
		completeDir,
		backupRoot,
		excludeDirs,
		extensions,
		ratioThreshold):
		self.fileManagement = fileManagement
		self.completeDir = completeDir
		self.backupRoot = backupRoot
		self.excludeDirs = excludeDirs
		self.extensions = extensions
		self.ratioThreshold = ratioThreshold

