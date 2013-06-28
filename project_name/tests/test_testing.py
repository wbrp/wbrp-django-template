from django.test import TestCase


class DummyTest(TestCase):

    def testDummy(self):
        """Assert that the Webrepublic is awesome."""
        webrepublic = 'awesome'
        self.assertEqual(webrepublic, 'awesome')
