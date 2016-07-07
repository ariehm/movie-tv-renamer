import subprocess
import shutil
import os

class Renamer:
	def getRenamePath(self, contentFile):
		return os.path.join(
			self.__renameRoot, 
			contentFile.getCosmeticDir(), 
			contentFile.getCosmeticFileName())

	def __init__(self, renameRoot):
		self.__renameRoot = renameRoot

class SymLinkRenamer(Renamer):
	def renameFile(self, contentFile):
		os.symlink(
			contentFile.fullName, 
			os.path.splitext(self.getRenamePath())[0])

	def __init__(self, renameRoot):
		Renamer.__init__(self, renameRoot)

class CopyRenamer(Renamer):
	def renameFile(self, contentFile):
		shutil.copyfile(contentFile.fullName, self.getRenamePath())

	def __init__(self, renameRoot):
		Renamer.__init__(self, renameRoot)
