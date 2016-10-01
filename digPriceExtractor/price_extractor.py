# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-21 12:36:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-30 23:39:47

import copy 
import types
from digExtractor.extractor import Extractor
from digPriceExtractor.digpe import DIGPE

class PriceExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']  # ? renamed_input_fields

    def extract(self, doc):
        digpe = DIGPE()
        return digpe.extract(doc['text'])
        
    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields

    def set_renamed_input_fields(self, renamed_input_fields):
        if not (isinstance(renamed_input_fields, basestring) or isinstance(renamed_input_fields, types.ListType)):
            raise ValueError("renamed_input_fields must be a string or a list")
        self.renamed_input_fields = renamed_input_fields
        return self 

