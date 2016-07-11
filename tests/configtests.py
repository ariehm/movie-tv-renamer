import os
import unittest
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

from config import ConfigSerializer

class ConfigSerializerTests(unittest.TestCase):
	def test_use_default_value_for_configs_not_specified(self):

	def test_happy(self):

