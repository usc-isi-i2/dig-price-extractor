# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 11:29:35
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-11-11 15:58:18

from preprocessor import ZEPreprocessor
from extractor import ZEExtractor
from normalizer import ZENormalizer
from unit import * 
import re


PE_DICT_NAME_PRICE = 'price'
PE_DICT_NAME_PPH = 'price_per_hour'

PE_JSON_NAME_PRICE = 'price'
PE_JSON_NAME_PRICE_UNIT = 'price_unit'
PE_JSON_NAME_TIME_UNIT = 'time_unit'

class DIGPriceExtractor():

    def __init__(self):
        self.preprocessor = ZEPreprocessor()
        self.extractor = ZEExtractor()
        self.normalizer = ZENormalizer()

    re_digits = re.compile(r'\d+')
    re_alphabet = re.compile(r'[a-z ]+')

    def extract(self, text):
        cleaned_text_list = self.preprocessor.preprocess(text)
        extracted_text_list = self.extractor.extract_from_list(cleaned_text_list)
        normalized_text_list = self.normalizer.normalize_from_list(extracted_text_list)
        ans = {}
        ans.setdefault(PE_DICT_NAME_PRICE, [])
        # ans.setdefault(PE_DICT_NAME_PPH, [])

        price_per_hour = []
        price_n_hour = []
        price_half_hour = []

        # import json
        # print json.dumps(cleaned_text_list, indent=4)
        for normalized in normalized_text_list:
            if not normalized[PE_JSON_NAME_TIME_UNIT]:
                # ans[PE_DICT_NAME_PPH].append(normalized[PE_JSON_NAME_PRICE])
                price_per_hour.append(int(normalized[PE_JSON_NAME_PRICE]))
            else:
                tunit = DIGPriceExtractor.re_alphabet.findall(normalized[PE_JSON_NAME_TIME_UNIT])
                if tunit and tunit[0].strip() in UNIT_TIME_HOUR:
                    digits = DIGPriceExtractor.re_digits.findall(normalized[PE_JSON_NAME_TIME_UNIT])
                    if not digits or int(digits[0]) == 1:
                        price_per_hour.append(int(normalized[PE_JSON_NAME_PRICE]))
                        # ans[PE_DICT_NAME_PPH].append(normalized[PE_JSON_NAME_PRICE])
                    elif digits and digits[0] > 1 and digits[0] <= 20:
                        price_n_hour.append(int(normalized[PE_JSON_NAME_PRICE]/digits[0]))
                print tunit
                if tunit and tunit[0].strip() in UNIT_TIME_HALF_HOUR:
                    price_half_hour.append(2*int(normalized[PE_JSON_NAME_PRICE]))

            ans[PE_DICT_NAME_PRICE].append(normalized)

        if price_per_hour:
            pph_list = price_per_hour
        else:
            pph_list = price_n_hour + price_half_hour

        ans[PE_DICT_NAME_PPH] = str(1*sum(pph_list)/len(pph_list)) if len(pph_list) else ''
        # else:


        # # load price per hour data
        # price_per_hour = []
        # # ['full hour', 'full hr', 'f hour', 'f hr', 'f h', 'fh', 'hourly', 'hour', 'hr', 'h']
        # for hd in hour_data:    
        #     # hour_data: contain data without time_unit or belongs time unit for hour
        #     digits = DIGPriceExtractor.re_digits.findall(hd[PE_JSON_NAME_TIME_UNIT])
        #     if not digits or int(digits[0]) == 1 or PE_JSON_NAME_TIME_UNIT in ['full hour', 'full hr', 'f hour', 'f hr', 'f h', 'fh', 'hourly', 'hour', 'hr', 'h']:
        #         price_per_hour.append(int(hd[PE_JSON_NAME_PRICE]))

        # print price_per_hour
        

        return ans

    def extract_from_list(self, text_list):
        return [self.extract(text) for text in text_list]


if __name__ == '__main__':
    text = "%100 Real Pics In/Outcall $150 hh- 21 - 21 \n \n \n 786-506-4729   Jun 05, 2013  Sexy Young Latina from Miami New in Town % 100 Real Pics in/out call - 21 \n \n \n 786-506-4729   May 09, 2013  Dime Escorts New Girls %100 Real Pics In/Outcall \n \n 786-506-4729   Apr 09, 2013  2 Girl Special April & Dime %100 Real Pics In/Outcall - 20 \n \n \n \n \n \n \n"

    dp = DIGPriceExtractor()
    ans = dp.extract(text)
    import json
    print json.dumps(ans, indent=4)
