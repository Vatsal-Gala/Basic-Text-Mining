#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:08:36 2017

@author: vatsalsmacbook
"""

# POS TAGS : NN|VB|JJ|RB|PRP + Lots More
# CHUNK TAGS : NP|VP
# CHUNK RELATIONS : NP-SUBJ|NP-OBJ
# RegEx fro sentences is not as fast as default method.

from scriptvariables import *
from pattern.en import parse,Text,Sentence

class WordSemantic(object):
    
    def __init__(self,data):
#        Don't convert to lower string as CAPS are important too. But Implement lower
        if isinstance(data,basestring):
            self.DATA = data
            self.PARSE = parse(self.DATA)
            self.DOC = Text(self.PARSE)
        
    @property
    def sentencelist(self):
        sentence_list = [x.string for x in self.DOC]
        return sentence_list
    
    @property
    def sentencelist_(self):
        return self.DOC
    
    @property
    def wordlist(self):
        word_list = self.wordlist_
        return_list = [x.string for x in word_list]
        return return_list
        
    @property
    def wordlist_(self):
        return self.DOC.words
    
    def wordset(self,kind_of_word):
        kind_of_word = kind_of_word()
        word_list = self.wordlist_
        return_list = []
        for word in word_list:
            if kind_of_word in word.type:
                return_list.append(word)
        return return_list
    
    @property
    def chunklist_(self):
        sentence_obj = Sentence(self.PARSE)
        return sentence_obj.chunks

    @property
    def chunklist(self):
        chunk_list = self.chunklist_
        return [x.string for x in chunk_list]
        
    def chunkset(self,kind):
        kind = kind()
        chunk_obj_list = self.chunklist_
        return [chunk for chunk in chunk_obj_list if kind in chunk.type]
    