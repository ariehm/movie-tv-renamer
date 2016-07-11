import json
import os

class Config:
	def __init__(
		self,
		fileManagement='SymLinks',
		completeDir='complete',
		backupRoot='backup',
		excludeDirs=[],
		extensions=['.mkv', '.mp4', '.ts', '.mov', '.avi'],
		ratioThreshold=2):
		self.fileManagement = fileManagement
		self.completeDir = completeDir
		self.backupRoot = backupRoot
		self.excludeDirs = excludeDirs
		self.extensions = extensions
		self.ratioThreshold = ratioThreshold

class ConfigSerializer:
	def serializeConfig(self, config, configFilePath):
		with open(configFilePath) as f:
			json.dump(config, f)

	def deserializeConfig(self, configFilePath):
		configJson = None

		with open(configFilePath) as f:
			configJson = json.load(f)

		ret = Config(
			configJson['fileManagement'],
			configJson['completeDir'],
			configJons['backupRoot'],
			configJons['excludeDirs'],
			configJons['extensions'],
			configJons['ratioThreshold'])

