from django.test import TestCase

class SmokeTest (TestCase):
  def test_BadMath(self):
    self.assertEqual(1+1,3)


