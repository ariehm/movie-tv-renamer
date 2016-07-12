import json
import os

class Config:
	CLIENT_KEY = 'client'
	FILE_MANAGEMENT_KEY = 'file-management'
	COMPLETE_DIR_KEY = 'complete-dir'
	BACKUP_ROOT_KEY = 'backup-root'
	EXCLUDE_DIRS_KEY = 'exclude-dirs'
	EXTENSIONS_KEY = 'extensions'
	RATIO_THRESHOLD_KEY = 'ratio-threshold'

	CLIENT_DEFAULT = 'transmission'
	FILE_MANAGEMENT_DEFAULT = 'symlinks'
	COMPLETE_DIR_DEFAULT = 'complete'
	BACKUP_ROOT_DEFAULT = 'backup'
	EXCLUDE_DIRS_DEFAULT = []
	EXTENSIONS_DEFAULT = ['.mkv', '.mp4', '.ts', '.mov', '.avi']
	RATIO_THRESHOLD_DEFAULT = 2

	@staticmethod
	def getDefaultConfig():
		return Config(
			Config.CLIENT_DEFAULT,
			Config.FILE_MANAGEMENT_DEFAULT,
			Config.COMPLETE_DIR_DEFAULT,
			Config.BACKUP_ROOT_DEFAULT,
			Config.EXCLUDE_DIRS_DEFAULT,
			Config.EXTENSIONS_DEFAULT,
			Config.RATIO_THRESHOLD_DEFAULT)

	@staticmethod
	def loadFromFile(serializer, filePath):
		deserializedDict = serializer.deserializeFromFile(filePath)

		client = Config.CLIENT_DEFAULT
		fileManagement = Config.FILE_MANAGEMENT_DEFAULT
		completeDir = Config.COMPLETE_DIR_DEFAULT
		backupRoot = Config.BACKUP_ROOT_DEFAULT
		excludeDirs = Config.EXCLUDE_DIRS_DEFAULT
		extensions = Config.EXTENSIONS_DEFAULT
		ratioThreshold = Config.RATIO_THRESHOLD_DEFAULT

		if Config.CLIENT_KEY in deserializedDict:
			client = deserializedDict[Config.CLIENT_KEY]
		if Config.FILE_MANAGEMENT_KEY in deserializedDict:
			fileManagement = deserializedDict[Config.FILE_MANAGEMENT_KEY]
		if Config.COMPLETE_DIR_KEY in deserializedDict:
			completeDir = deserializedDict[Config.COMPLETE_DIR_KEY]
		if Config.BACKUP_ROOT_KEY in deserializedDict:
			backupRoot = deserializedDict[Config.BACKUP_ROOT_KEY]
		if Config.EXCLUDE_DIRS_KEY in deserializedDict:
			excludeDirs = deserializedDict[Config.EXCLUDE_DIRS_KEY]
		if Config.EXTENSIONS_KEY in deserializedDict:
			extensions = deserializedDict[Config.EXTENSIONS_KEY]
		if Config.RATIO_THRESHOLD_KEY in deserializedDict:
			ratioThreshold = deserializedDict[Config.RATIO_THRESHOLD_KEY]

		return Config(
			client,
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
		client,
		fileManagement,
		completeDir,
		backupRoot,
		excludeDirs,
		extensions,
		ratioThreshold):
		self.client = client
		self.fileManagement = fileManagement
		self.completeDir = completeDir
		self.backupRoot = backupRoot
		self.excludeDirs = excludeDirs
		self.extensions = extensions
		self.ratioThreshold = ratioThreshold

