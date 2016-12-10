# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-01 13:17:49
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-12-10 00:20:57

import re

from unit import *

class ZEExtractor():

    re_digits = re.compile(r'\d+')
    re_alphabet = re.compile(r'[a-z]+')

    prefix = r'(?:(?<=[\A\b\s])|^)'
    postfix = r'(?:(?=[\Z\b\s])|$)'
    # postfix = r'(?=[\Z\s])'

    reg_time_units = \
        prefix + \
        r'(?:' + \
        r'(?:\d{1,3}[ ]?(?:' + r'|'.join(UNIT_TIME_HOUR + UNIT_TIME_MINUTE) + r'))' + \
        r'|' + \
        r'(?:' + r'|'.join(UNIT_TIME_UNITS) + r')' + \
        r')' + \
        postfix

    reg_separator = r'[\t ]?'
    reg_price_digit = r'\b\d{1,3}\b'    # r'\d{1,4}' 
    reg_price_unit = r'(?:' + r'|'.join(UNIT_PRICE_UNITS) + r'){0,2}'  # \b
    reg_interval = r'\w{,30}'

    # patterns

    # pattern for # time
    reg_price_time = r'(?:' + \
        reg_price_unit + \
        reg_separator + \
        reg_price_digit + \
        reg_separator + \
        reg_price_unit + \
        reg_separator + \
        r'(?:' + reg_separator + r'for' + reg_separator + r')?' + \
        reg_separator + \
        reg_time_units + \
        r')'

    re_price_time = re.compile(reg_price_time)
    # r'(?:=(?:[a-z]+[\t ]){,5}?|[\t ]?)' + \
    # r'(?:' + reg_separator + r'for' + reg_separator + r')?' + \

    ## pattern for time #
    reg_time_price = r'(?:' + \
        reg_time_units + \
        reg_separator + \
        reg_price_unit + \
        reg_separator + \
        reg_price_digit + \
        reg_separator + \
        reg_price_unit + \
        ')'
    re_time_price = re.compile(reg_time_price)

    # pattern for price digits only
    reg_only_price = r'(?:' + \
        reg_price_unit + \
        reg_separator + \
        reg_price_digit + \
        reg_separator + \
        reg_price_unit + \
        ')'
    re_only_price = re.compile(reg_only_price)

    reg_combine = re.compile(
        r'(?:' + r'|'.join([reg_time_price, reg_price_time]) + r')')

    def filter(self, text_list):
        ans = []

        for text in text_list:
            if '$' in text:
                ans.append(text)
                continue

            if ZEExtractor.re_alphabet.findall(text):
                digits = ZEExtractor.re_digits.findall(text)
                if len(digits) == 1 and int(digits[0]) < 5:
                    continue
                ans.append(text)
        return ans

    def load_most_potential_target(self, pool):
        def contain_time_unit(text):
            for tu in UNIT_TIME_UNITS:
                if tu in text:
                    return True
            return False

        def contain_price_unit(text):
            for pu in UNIT_PRICE_UNITS:
                if pu in text:
                    return True
            return False

        count_length_array = [sum([len(item) for item in _ if not item.strip().isdigit()]) for _ in pool]
        count_token_array = [len([item for item in _ if not item.strip().isdigit()]) for _ in pool]
        count_dollar_array = [len([item for item in _ if item if '$' in item]) for _ in pool]
        count_time_price_unit = [len([item for item in _ if contain_time_unit(item) and contain_price_unit(item)]) for _ in pool]

        # print count_length_array
        # print count_token_array
        # print count_dollar_array
        # print count_time_price_unit


        scores = [0]*len(pool)
        weights = [.1,.2,.2,.5]
        for _ in [count_length_array, count_token_array, count_dollar_array, count_time_price_unit]:
            for i in range(len(scores)):
                scores[i] += _[i]*weights[i]

        # print scores

        return pool[scores.index(max(scores))]

    def extract(self, text):
        text_pt_ext = ZEExtractor.re_price_time.findall(text)
        text_tp_ext = ZEExtractor.re_time_price.findall(text)
        text_op_ext = ZEExtractor.re_only_price.findall(text)        

        if len(text_pt_ext) > len(text_tp_ext):
            target = text_pt_ext
        elif len(text_pt_ext) < len(text_tp_ext):
            target = text_tp_ext
        else:
            pool = [text_tp_ext, text_pt_ext, text_op_ext]
            target = self.load_most_potential_target(pool)
        # print target
        extra = []
        target_digits = ZEExtractor.re_digits.findall(' '.join(target))

        for op_ext in text_op_ext:
            for opd in ZEExtractor.re_digits.findall(op_ext):
                if opd in target_digits:
                    break
                else:
                    extra.append(op_ext)
                    break
        target += extra
        return self.filter(target)

    def extract_from_list(self, text_list):
        extracted_text_list = [self.extract(
            cleaned_text) for cleaned_text in text_list]
        extracted_text = [val.strip()
                          for sublist in extracted_text_list for val in sublist]
        return extracted_text
