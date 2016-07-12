import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from mrclean import MrClean

class ShouldExecuteCommand:
    def shouldExecute(self, filePath):
        return True

    def executeClean(self, filePath):
        pass

class ShouldNotExecuteCommand:
    def shouldExecute(self, filePath):
        return False

    def executeClean(self, filePath):
        pass

class FailureCommand:
    def shouldExecute(self, filePath):
        return True

    def executeClean(self, filePath):
        assert False, 'This command always fails'

class MrCleanTests(unittest.TestCase):
    def setUp(self):
        self.__executed = False

    def test_all_should_clean(self):
        cmds = (ShouldExecuteCommand(),ShouldExecuteCommand(),ShouldExecuteCommand())

    def test_execute_none_if_not_all_should_clean(self):
        cmds = (ShouldExecuteCommand(),ShouldNotExecuteCommand(),FailureCommand())
