import os
import sys
import time
import json
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digPriceExtractor.digpe import DIGPriceExtractor


class TestPriceExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_price_extractor(self):
        # text = "Good morning I\'m doing incalls only gentleman I\'m quick 60 roses ?Hhr 80 roses ?Hour 120 roses unrushed and f.service provided nonnegotiable donations  614-563-3342"
        # text = "hello world 120 hour."
        # text = "hello world rose 6 hour "
        text = "hello world 213-379-0691 hour."
        dp = DIGPriceExtractor()
        ans = dp.extract(text)
        print json.dumps(ans, indent=4)

    

if __name__ == '__main__':
    unittest.main()



