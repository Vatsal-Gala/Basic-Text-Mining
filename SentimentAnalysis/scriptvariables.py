#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Make variables for RegularExpressions ################# 
"""
Created on Mon Sep  4 13:32:45 2017

@author: vatsalsmacbook
"""
# Word Variables
def ADJECTIVE():
    return 'JJ'

def VERB():
    return 'VB'

def ADVERB():
    return 'RB'

def NOUN():
    return 'NN'

def PRONOUN():
    return 'PRP'

def MODAL():
    return 'MD'

def EXISTENTIAL():
    return 'EX'

def DETERMINER():
    return 'DT'

def NUMBER():
    return 'CD'

def CONJUCTION():
    return 'CC'

def WH():
    return 'W'

def PUNCT():
    return '.'

def COMMA():
    return ','

# Chunk / Phrase Variables
def NOUNPHR():
    return 'NP'

def PREPOSPHR():
    return 'PP'

def VERBPHR():
    return 'VP'

def ADVERBPHR():
    return 'ADVP'

def ADJECTIVEPHR():
    return 'ADJP'

def SUBCONJPHR():
    return 'SBAR'

def PARTICLEPHR():
    return 'PRT'

def INTERJECTIONPHR():
    return 'INTJ'

def PREPNOUNPHR():
    return 'PNP'

def ALLPHR():
    return ''

# Relation Tag Variables
def SUBJECT():
    return '-SBJ'

def OBJECT():
    return '-OBJ'

def PREDICATE():
    return '-PRD'

def TEMPORAL():
    return '-TMP'

def CLOSELYRELATED():
    return '-CLR'

def LOCATION():
    return '-LOC'

def DIRECTION():
    return '-DIR'

def EXTENT():
    return '-EXT'

def PURPOSE():
    return '-PRP'

# Language Variables
def ENGLISH():
    return 'en' 

# Regex Variables
    
def WORD():
    return r'\b(?:[\w]+!+)|\b(?:[\w]+\?+)|\b(?:[a-zA-Z0-9]\.){2,}|\w+(?:-+\w+)+|(?=\S+[\'])(?:[a-zA-Z\']+)+|\w+'

def SENTENCE():
    return r'[\w ,-]*?(?:[\(\{\[]+.*?[\)\}\]]+)*[\w ,-]*?[.!?]'

def BRACKETS():
    return r'[\(\{\[]+.*?[\)\}\]]+'

def ACRONYMS():
    return r'\b(?:[a-zA-Z0-9]\.){2,}'

def EXCLAIMS():
    return r'\b(?:[\w]+!+)|\b(?:[\w]+\?+)'

def HYPHENATED():
    return r'\w+(?:-+\w+)+'

def APOSTROPHES():
    return r'(?=[\S]+[\'\"])(?:[\S]*[\'\"]*)|(?:[\'\"]\S+)'

def  HYPHENSANDAPOSTROPHESE():
    return r'(?=\S*[\'-])(?:[a-zA-Z\'-]+)'
            
def COMPLEXSENTENCE():
    return r'[^.!?\s][^.!?]*(?:[.!?](?![\'\"]?\s|$)[^.!?]*)*[.!?]?[\'\"]?(?=\s|$)'


"""
pluralize              : return plural form of word
singularize            : return singular form of the word
comparative (adj only) : return comaprative form of adj
superlative (adj only) : return superlative form of adj
lemma                  : base form
lexeme      (vrb only) : possible forms
number                 : string to number
numerals(n,round = *)  : number to string
suggest                : spelling suggestions for a particular word
ngrams(data, n = *)    : give a list of ngrams
parse (tokenize,tags,
    chunks, relations) : breaks the sentence into words and give 
                         the concerning results
mood                   : returns INDICATIVE | IMPERATIVE 
                         | CONDITIONAL | SUBJUNCTIVE
synsets                : has 
                            pos      : Parts-of-speech
                            synonyms : similar meanings
                            gloss    : definition string
                            lexname  : category string
                            ic       : information content
                            antonym  : semantic oposite
                            hypernym : parent
                            hypernyms - (recursive : up and down, depth)
                            hyponyms : 
                            meronyms() : member parts
                            holonyms() : of which it is member
                            similar()  : similar verb , adjective
wordnet                 : --can be other wordnets maybe ^^
                            ancestor(s1, s2)  : common ancestor
                            similarity(s1, s2): similarity between 2 words
                            
"""
print