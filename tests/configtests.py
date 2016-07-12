import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from config import Config

class MockSerializer:
	def serializeToFile(self, toSerialize, filePath):
		pass

	def deserializeFromFile(self, filePath):
		ret = {}
		
		ret[Config.FILE_MANAGEMENT_KEY] = 'a'
		ret[Config.COMPLETE_DIR_KEY] = 'b'
		ret[Config.EXCLUDE_DIRS_KEY] = ['exclude1', 'exclude2']
		ret[Config.RATIO_THRESHOLD_KEY] = 'c'

		return ret

class ConfigTests(unittest.TestCase):
	def test_use_default_value_for_configs_not_specified(self):
		config = Config.loadFromFile(MockSerializer(), '')

		self.assertEqual(config.backupRoot, Config.BACKUP_ROOT_DEFAULT)
		self.assertEqual(config.extensions, Config.EXTENSIONS_DEFAULT)
