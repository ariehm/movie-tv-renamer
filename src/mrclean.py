import os
import shutil
import files

class TransmissionCleanTrigger:
    def isTriggered(self, filePathToClean):
        # triggered if seed ratio above threshold or file is torrent is not active
        raise NotImplementedError()

    def __init__(self, ratioThreshold):
        self.__ratioThreshold = ratioThreshold

class TransmissionCleanExecutor:
    def executeClean(self, filePathToClean):
        raise NotImplementedError()

class CopyCleanExecutor:
    def executeClean(self, filePathToClean):
        os.remove(filePathToClean)            

class SymLinkCleanExecutor:
    def executeClean(self, filePathToClean):
        mediaFile = files.MediaFile(filePathToClean)
        mediaFile.getMediaInfo()

        backupLocation = os.path.join(
            self.__backupRoot, contentFile.getCosmeticDir(), 
            contentFile.getCosmeticFileName())

        shutil.move(filePathToClean, backupLocation)
        os.remove(os.path.splitext(backupLocation)[0])
                
    def __init__(self, backupRoot):
        self.__backupRoot = backupRoot

class MrClean:
    def clean(self, filePathsToClean):
        for filePath in filePathsToClean:
            if self.__trigger == None or self.__trigger.isTriggered(filePath):
                self.__executor.executeClean(filePath)

    def __init__(self, executor, trigger = None):
        self.__executor = executor
        self.__trigger = trigger
