#!/usr/bin/env python
import unittest

loader = unittest.TestLoader()
start_dir = 'src/main/python'
suite = loader.discover(start_dir, "*.py")

runner = unittest.TextTestRunner()
runner.run(suite)
