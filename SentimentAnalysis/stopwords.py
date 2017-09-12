#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 22:18:42 2017

@author: vatsalsmacbook

File_description : creates a loadedlist of stopwords for a particular language base.
Also contains upde functions for a stopword list for dynamic stopword list creation.
"""
import re

class StopWords(object):

    def __init__(self, lang, context = ''):
        self.TYPE = lang()
        self.STOPWORDLIST = self.load(self.TYPE)
        self.CONTEXT = context

    def load(self, lang):
        """ Loads and returns a list of all the stopword file for the particular language passed as lang"""
        
        with open('stp_resources/stopwords_' + lang + '.txt', 'r') as file:
            return_list = []
            file_string = file.read()
            regex_result = re.findall(r'\w+', file_string)
            temp = set()
            return_list = [x for x in regex_result if x not in temp and (temp.add(x) or True)]
            
        return return_list

    def remove_stopwords(self, data, removecardinals=False, removeordinals=False):
        """Standard procedure removing of stopwords"""
        
#       lower implementation directly in comparision.
        temp_data = [x for x in data if x.lower() not in self.STOPWORDLIST]
        if(removecardinals):
            rmc = re.compile(r'^[0-9]+$') #change it to accept all numbers
            temp_data = [x for x in temp_data if not rmc.match(x)]
        if(removeordinals):
            rmo = re.compile(r'[0-9]+(?=)[th|nd|st|rd]+')
            temp_data = [x for x in temp_data if not rmo.match(x)]
        temp_data = [x for x in temp_data if len(x) > 2]
        
        return temp_data
    
    def _update_stopwords(self,update_list):
        """ Update the current self.STOPWORDLIST by adding the relevant new stopwords"""
        pass
    
    def find_stopwords(self,data):
        """ Will try and find some kind of stop words in the given data that don't amount to much """
#        Algorithm that finds stop words by taking data as input and giving
#       update_list as a list of stop words
        update_list = []
        self._update_stopwords(update_list)
        pass


