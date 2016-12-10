# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-21 12:36:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-11-13 15:35:08

import copy
from digExtractor.extractor import Extractor
from digPriceExtractor.digpe import DIGPriceExtractor

class PriceExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = 'text'
        self.digpe = DIGPriceExtractor()

    def extract(self, doc):
        if 'text' in doc:
            price = self.digpe.extract(doc['text'])
            if price['price'] or\
               price['price_per_hour']:
                return price
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields
