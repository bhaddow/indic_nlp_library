#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:42:55 2019

@author: fkirefu
"""



common_exceptions = {'Rs.' :{'asm':'',
                             'bn':'',
                             'gu':'રૂ.',
                             'hi':'रु.',
                             'kn':'ರೂ.',
                             'ml':'',
                             'mni': '', 
                             'mr':'रु.',
                             'ory':'',
                             'pa':'',
                             'ta':'ரூ.',
                             'te':'రూ.'  ,
                             'ur': ''},
                     'Dr.' : {'asm':'',
                             'bn':'',
                             'gu':'',
                             'hi':'डॉ.',
                             'kn':'',
                             'ml':'',
                             'mni': '', 
                             'mr':'डॉ.',
                             'ory':'',
                             'pa':'ਡਾ.',
                             'ta':'',
                             'te':'',
                             'ur': ''},
                    'Mr.': {'asm':'',
                             'bn':'',
                             'gu':'',
                             'hi':'',
                             'kn':'',
                             'ml': 'ശ്രീ.',
                             'mni': '', 
                             'mr':'श्री.',
                             'ory':'',
                             'pa':'',
                             'ta':'திரு.',
                             'te':'శ్రీ.',
                             'ur':''}}
                     
                     

others =  {'asm':['',],
             'bn':['',],
             'gu':['',],
             'hi':['टी.वी.',  # T.V. 
                   ],
             'kn':['',],
             'ml':['',],
             'mni': ['',], 
             'mr':['',],
             'ory':['',],
             'pa':['',],
             'ta':['',],
             'te':['',],
             'ur':['',]}


hindi_eng_phonetics =  {'A.': 'ए.', # Is Marathi the same?
                         'B.': 'बी.',
                         'C.': 'सी.',
                         'D.': 'डी.',
                         'E.': 'ई.',
                         'F.': 'ऐफ.',
                         'G.': 'जी.',
                         'H.': 'एच.',
                         'I.': 'आइ.',
                         'J.': 'जे.',
                         'K.': 'के.',
                         'L.': 'ऐल.',
                         'M.': 'ऐम.',
                         'N.': 'ऐन.',
                         'O.': 'ओ.',
                         'P.': 'पी.',
                         'Q.': 'क्यू.',
                         'R.': 'आर.',
                         'S.': 'एस.',
                         'T.': 'टी.',
                         'U.': 'यू.',
                         'V.': 'वी.',
                         'W.': 'डब्ल्यू.',
                         'X.': 'ऐक्स.',
                         'Y.': 'वाय.',
                         'Z.': 'ज़ैड.' }



# may need eng_phon rules: mr ,te, ta, ory, kn, 

# probably don't need phon rules: ur




