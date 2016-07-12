import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

import main
import renamers
from config import Config

class MainTests(unittest.TestCase):
    def test_get_options_happy(self):
        options = main.getOptions(['-c', 'asdf'])

        self.assertEqual(options, {'c': 'asdf'})

    def test_get_config_no_path(self):
        config = main.getConfigs('')

        # assert that a config with default values is returned
        self.assertEqual(config.backupRoot, Config.BACKUP_ROOT_DEFAULT)
        self.assertEqual(config.completeDir, Config.COMPLETE_DIR_DEFAULT)

    def test_get_config_invalid_path(self):
        config = main.getConfigs('not/a/real/config/file')

        # assert that a config with default values is returned
        self.assertEqual(config.backupRoot, Config.BACKUP_ROOT_DEFAULT)
        self.assertEqual(config.completeDir, Config.COMPLETE_DIR_DEFAULT)

    def test_get_config_happy(self):
        config = main.getConfigs('test-filesystem/test-config')

        # assert that a config with default values is returned
        self.assertEqual(config.backupRoot, Config.BACKUP_ROOT_DEFAULT)
        self.assertEqual(config.completeDir, Config.COMPLETE_DIR_DEFAULT)
        self.assertEqual(config.ratioThreshold, 345)

    def test_dependencies_use_copy(self):
        config = Config.getDefaultConfig()
        config.fileManagement = 'copy'
        deps = main.getDependencies(config)

        print(deps['renamer'])
        self.assertTrue(isinstance(deps['renamer'], renamers.CopyRenamer))

    def test_dependencies_use_symlink(self):
        deps = main.getDependencies(Config.getDefaultConfig())

        self.assertTrue(isinstance(deps['renamer'], renamers.SymLinkRenamer))

