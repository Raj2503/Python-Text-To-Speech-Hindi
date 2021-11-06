import unittest

from synthme import util

class TestUtil(unittest.TestCase):
  def test_get_pronunciation(self):
    self.assertEqual(util.get_pronunciation("me"), [28, 7])
  def test_tokenize(self):
    self.assertEqual(util.tokenize("test message"), ["test", "message"])
    self.assertEqual(util.tokenize("test"), ["test"])
    self.assertEqual(util.tokenize(""), [])