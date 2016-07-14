import subprocess
import shutil
import os
import logging

class Renamer:
    def getRenamePath(self, contentFile):
        return os.path.join(
            self.renameRoot, 
            contentFile.getCosmeticDir(), 
            contentFile.getCosmeticFileName())

    def __init__(self, renameRoot):
        self.renameRoot = renameRoot

class SymLinkRenamer(Renamer):
    def __shouldRename(self, renamePath):
        return not os.path.exists(renamePath)

    def renameFile(self, contentFile):
        log = logging.getLogger('root')

        renameDir = os.path.join(self.renameRoot, contentFile.getCosmeticDir())
        if not os.path.exists(renameDir):
            os.makedirs(renameDir)

        renamePath = os.path.splitext(self.getRenamePath(contentFile))[0]

        if not self.__shouldRename(renamePath):
            log.info('SymLink {%s} already exists', renamePath)
            return

        log.info('Creating SymLink at {%s} to {%s}', renamePath, contentFile.fullName)
        os.symlink(contentFile.fullName, renamePath)

    def __init__(self, renameRoot):
        Renamer.__init__(self, renameRoot)

class CopyRenamer(Renamer):
    def __shouldRename(self, renamePath):
        return not os.path.exists(renamePath)

    def renameFile(self, contentFile):
        log = logging.getLogger('root')

        renameDir = os.path.join(self.renameRoot, contentFile.getCosmeticDir())
        if not os.path.exists(renameDir):
            os.makedirs(renameDir)

        renamePath = self.getRenamePath(contentFile)

        if not self.__shouldRename(renamePath):
            log.info('Renamed file {%s} already exists', renamePath)
            return

        log.info('Copying {%s} to {%s}', renamePath, contentFile.fullName)
        shutil.copyfile(contentFile.fullName, renamePath)

    def __init__(self, renameRoot):
        Renamer.__init__(self, renameRoot)
