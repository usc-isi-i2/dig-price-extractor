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
        text = "\n \n \n \n \n \n Escort's Phone: \n \n \n786-506-4729  \n \n Escort's Location: \nMiami, Florida  \n Escort's Age:   21   Date of Escort Post:   Oct 26th 9:01am \n REVIEWS:   \n REVIEWS FOUND!!! READ BEFORE YOU CALL   \n \n \n \n \n \nThere are  49  girls looking in  Buffalo .\n VIEW GIRLS \n \nDime Piece My Name Is Dime I'll assure You With Me You'll Have An Unforgettable Time No need To Hide Let The Freak In you Shine Come On This Ride NO EXCHANGE OF PICS Feel Free to FaceTime 7865064729 Donations $150/30m  $200 full hour (Unrushed) 420 INCALL & OUTCALLS-TODAY 7865064729. Call  786-506-4729 . I offer video/photo also, ask me on my profile before calling...  EasySex \n   \n \n   \n \n   \n Call me on my cell at 786-506-4729. Date of ad: 2014-10-26 09:01:00 \n More posts from  786-506-4729 \n 786-506-4729   Dec 05, 2014  UNFORGETTABLE petite FLEXiABLE Latina R2P - 21 \n \n \n 786-506-4729   Dec 03, 2014  100QVSLiM SEXi SLiNDERBack In Your Area - 21 \n \n \n 786-506-4729   Nov 29, 2014  NEW KiTYY ALERT R2P 18yrs Young - 18 \n \n \n 786-506-4729   Nov 15, 2014  100qsSiZZiLiNG HOT LATiNAFantasyGirl - 21 \n \n \n 786-506-4729   Nov 03, 2014  iM BACK Small Sexy Petite100Qs NewPics \n \n \n 786-506-4729   Oct 10, 2014  NEW GIRLS HAVE 1or BOTH The Choice Is Urs - 19 \n \n \n 786-506-4729   Sep 18, 2014  PuertoRican Barbie Small Slender SexyCALL ME IM WAITING... - 21 \n \n \n 786-506-4729   Sep 17, 2014  IM BACKKK Playmate Latina4'9 Bubble Butt R2P - 21 \n \n \n 786-506-4729   Sep 11, 2014  PYT FROM MIAMI LIMITED TIME ONLY. 4'9 petite Latina - 21 \n \n \n 786-506-4729   Aug 07, 2014  Sexay Mami - 21 \n \n \n 786-506-4729   Jun 29, 2014  LATINA FROM MIAMI IN TOWN 1DAY catch me if you can. NewPICS&VIDim waiting. - 21 \n \n \n 786-506-4729   Aug 21, 2013  SEXY LATINA no fake pics %100 real in/outcall - 20 \n \n \n 786-506-4729   Jul 31, 2013  Young & Sexy Latina - 20 \n \n \n 786-506-4729   Jul 20, 2013  Dime Piece %100 Real Pics In/Outcall $150 hh $200 h - 21 \n \n \n 786-506-4729   Jul 04, 2013  Dime Piece %100 Real Pics In/Outcall $150 hh $200 h - 21 - 21 \n \n \n 786-506-4729   Jun 05, 2013  Sexy Young Latina from Miami New in Town % 100 Real Pics in/out call - 21 \n \n \n 786-506-4729   May 09, 2013  Dime Escorts New Girls %100 Real Pics In/Outcall $200 - 21 \n \n \n 786-506-4729   Apr 09, 2013  2 Girl Special April & Dime %100 Real Pics In/Outcall - 20 \n \n \n \n \n \n \n"
        dp = DIGPriceExtractor()
        ans = dp.extract(text)
        print json.dumps(ans, indent=4)

    

if __name__ == '__main__':
    unittest.main()



