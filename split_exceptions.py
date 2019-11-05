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


phonetics = {"hi" : hindi_eng_phonetics}

#
# Create Moses non-breaking prefix files for Indic languages
# (probably doesn't belong in this repo - do not merge)
#

import argparse
import logging
import os
import os.path
import sys



LOG = logging.getLogger(__name__)
LANGS = ["hi"]

def main():
  logging.basicConfig(format='%(asctime)s %(levelname)s: %(name)s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
  parser = argparse.ArgumentParser()
  parser.add_argument("-o", "--output-dir", default="nbp")
  args = parser.parse_args()

  if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)


  for lang in LANGS:
    with open("{}/nonbreaking_prefix.{}".format(args.output_dir, lang), "w") as ofh:
      print("#Anything in this file, followed by a period (and an upper-case word), does NOT indicate an end-of-sentence marker.", file=ofh)
      print(file=ofh)
      print("#common exceptions", file=ofh)
      for key, excepts in common_exceptions.items():
        nbp = excepts.get(lang,"")
        if nbp:
          print("# " + key[:-1], file=ofh)
          print(nbp[:-1], file=ofh)
      print(file=ofh)

      print("#others", file=ofh)
      for nbp in others.get(lang, []):
        print(nbp[:-1], file=ofh)
      print(file=ofh)

      print("#phonetics", file=ofh)
      for key,nbp in sorted(phonetics.get(lang,{}).items()):
        print("# " + key[:-1], file=ofh)
        print(nbp[:-1], file=ofh)
      print(file=ofh)


if __name__ == "__main__":
  main()



