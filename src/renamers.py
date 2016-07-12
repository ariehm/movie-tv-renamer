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
    def __shouldRename(self, renamePath):
        return not os.path.exists(renamePath)

    def renameFile(self, contentFile):
        renamePath = os.path.splitext(self.getRenamePath())[0]

        if not self.__shouldRename(renamePath):
            return

        os.symlink(contentFile.fullName, renamePath)

    def __init__(self, renameRoot):
        Renamer.__init__(self, renameRoot)

class CopyRenamer(Renamer):
    def __shouldRename(self, renamePath):
        return not os.path.exists(renamePath)

    def renameFile(self, contentFile):
        renamePath = self.getRenamePath()

        if not self.__shouldRename(renamePath):
            return

        shutil.copyfile(contentFile.fullName, renamePath)

    def __init__(self, renameRoot):
        Renamer.__init__(self, renameRoot)
