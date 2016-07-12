import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from mrclean import MrClean

executed = False

class TestException(Exception):
    pass

class AlwaysTrueTrigger:
    def isTriggered(self, filePath):
        return True

class AlwaysFalseTrigger:
    def isTriggered(self, filePath):
        return False

class Executor:
    def executeClean(self, filePath):
        print("a")
        self.executed = True

    def __init__(self):
        self.executed = False

class MrCleanTests(unittest.TestCase):
    def test_no_trigger(self):
        executor = Executor()
        MrClean(executor).clean(['a'])

        self.assertTrue(executor.executed)

    def test_is_triggered(self):
        executor = Executor()
        MrClean(executor, AlwaysTrueTrigger()).clean(['a'])
        
        self.assertTrue(executor.executed)

    def test_is_not_triggered(self):
        executor = Executor()
        MrClean(executor, AlwaysFalseTrigger()).clean(['a'])

        self.assertFalse(executor.executed)

