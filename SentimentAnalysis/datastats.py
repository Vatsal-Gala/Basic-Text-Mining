#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:45:03 2017

@author: vatsalsmacbook
"""

from scriptvariables import *
from collections import defaultdict
from wordsemantic import WordSemantic

class DataStats(WordSemantic):
    def __init__(self,doc,lang = None):
        self.lang = ENGLISH if lang is None else lang
        self.DOC = doc
        super(DataStats,self).__init__(self.DOC)
        self.ws_obj = WordSemantic(self.DOC)
        pass
#    change the fuctions to use objects instead of strings
    def phrase_freq(self):
        chunk_list = self.chunklist_
        freq_dict = self._entity_freq(data_list = chunk_list)
        return freq_dict
    
    def word_freq(self):
        word_list = self.wordlist_
        freq_dict = self._entity_freq(data_list = word_list)
        return freq_dict
    
    def _entity_freq(self,data_list):
        obj_tuple = {}
        for obj in data_list:
            obj_tuple[obj.string]=obj
        string_list = [obj.string for obj in data_list]
        freq_dict = defaultdict(int)
        for val in string_list:
            freq_dict[val]+=1
        return_list=[tuple([y,x,freq_dict[x]]) for x,y in obj_tuple.items()]
        return return_list

    
    def make_indistinct(self,data_list):
        """
        input format:
        (Word(u'all/DT'), u'all', 13),
        output format:
        (u'all', 13),
        BUT WITH CASE INDISTINCTION
        """
        new_list=defaultdict(int)
        for tupple in data_list:
            new_list[tupple[1].lower()] += tupple[2]
        return new_list.items()
            


# Imporve the class below 
#        based on the above improvisations
class SearchData(DataStats):
    def __init__(self,doc):
        super(SearchData,self).__init__(doc)
        pass
        
    def start_word(self,key):
        """
        function to find phrases or words that start with the given word = key (single implemetaion or multiple implementation)
        input : the
        output:
            single : the ball || there
            multiple : theball, there
            output of format : only string and freq (optional but insisted upon)
        """
        pass

    def contains_word(self, key):
        """
        same as start_word func, but instead of starting with the word may contain the key
        """
        pass
    
    def kind_of(self,kind):
        """
        function that returns all phrases, words belonging to a particular kind 
        eg : kind of noun , verb noun phrase, verb phrase
        input : kind of word
        being a sub class will access the methods and lists from super classes
        """
        pass
