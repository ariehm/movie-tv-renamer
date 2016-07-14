import os
import logging

from files import File

class ContentFinder:
    @staticmethod
    def getCompleteContentFilePaths(completeDir, excludeDirs, extensions):
        log = logging.getLogger('root')
        log.info('Search %s for content with extensions %s', completeDir, extensions)
        log.info('Do not look in %s directories', excludeDirs)

        completeFilePaths = []

        for root, subdirs, files in os.walk(completeDir):
            if any(d == root for d in excludeDirs):
                continue
            for file in files:
                completeFilePaths.append(os.path.join(root, file))

        # filter complete files for appropriate extensions
        ret = [f for f in completeFilePaths if f.endswith(tuple(extensions))]

        for f in ret:
            log.info('Found complete file {%s}', f)

        return ret
