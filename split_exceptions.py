#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:42:55 2019

@author: fkirefu
"""


common_exceptions = {'Rs' :{'asm':[], # probably doesn't exist, rupees are takkas টকা
                             'bn':[],  # probably doesn't exist, rupees are takkas টাকা
                             'gu':['રૂ'],
                             'hi':['रु'],
                             'kn':['ರೂ'],
                             'ml':[], # probably doesn't exist
                             'mni': [], # unsure if exists
                             'mr':['रु'],
                             'ory':[], # probably doesn't exist
                             'pa':[], # probably doesn't exist
                             'ta':'ரூ',
                             'te':'రూ'  ,
                             'ur': []}, # Very sure doesn't exist
                     'Dr' : {'asm':['ড'],
                             'bn':['ড'],
                             'gu':['ડો', 'ડૉ'],
                             'hi':['डॉ', 'डा'],
                             'kn':['ಡಾ'],
                             'ml':['ഡോ'],
                             'mni': ['দা'], 
                             'mr':['डॉ', 'डा'],
                             'ory':[], # probably doesnt exist
                             'pa':['ਡਾ', 'ਪ੍ਰੋ'], #  second one is actually Prof
                             'ta':[], # probably doesn't exist
                             'te':[],  # probably doesnt exist
                             'ur': []}, # Very sure doesn't exist
                    'Mr': {'asm':[], # don't think it exists
                             'bn':[],  # don't think it exists
                             'gu':['શ્રી'], #  'shri' very uncommon with full stop
                             'hi':['श्री'],  #  'shri' very uncommon with full stop
                             'kn':['ಶ್ರೀ'],
                             'ml': ['ശ്രീ'],  #  'shri'
                             'mni': [],  # don't think it exists
                             'mr':['श्री'],  #  'shri' uncommon with full stop
                             'ory':['ରୀ'],    # 'shri' does not actually exist with full stop in pmindia corpus
                             'pa':['ਸ੍ਰੀ'], #   'shri' uncommon with full stop
                             'ta':['திரு'],
                             'te':['శ్రీ'],
                             'ur':[]}} # Very sure doesn't exist
                     
                     

others =  {'asm':['',],
             'bn':['',],
             'gu':['',],
             'hi':['टीवी',  # TV 
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


# will need eng_phon rules: hi, mr ,te, ta, ory, kn, bn, asm, mni, pa, ml, gu
# done for                  hi , mr, te, ta, X   kn, bn, asm, mni,  pa,  ml, gu


# probably don't need phon rules: ur (because they don't have full stop after phonetic spelling)


# asm, bn, mni share same unicode

# hi and mr share same unicode

# ory, ur, kn, ml, gu, pa, ta, te, have their own


# we need single consonant alphabets for: hi, gu, kn, mr, ory, pa


# probably don't need for: asm, bn, mni, ur, ml, ta, te


hi_mr_single_cons = ['क',
                             'ख',
                             'ग',
                             'घ',
                             'ङ',
                             'च',
                             'छ',
                             'ज',
                             'झ',
                             'ञ',
                             'ट',
                             'ठ',
                             'ड',
                             'ढ',
                             'ण',
                             'त',
                             'थ',
                             'द',
                             'ध',
                             'न',
                             'प',
                             'फ',
                             'ब',
                             'भ',
                             'म',
                             'य',
                             'र',
                             'ल',
                             'व',
                             'श',
                             'ष',
                             'स',
                             'ह']

gu_single_cons = ['ક',
                 'ખ',
                 'ગ',
                 'ઘ',
                 'ઙ',
                 'ચ',
                 'છ',
                 'જ',
                 'ઝ',
                 'ઞ',
                 'ટ',
                 'ઠ',
                 'ડ',
                 'ઢ',
                 'ણ',
                 'ત',
                 'થ',
                 'દ',
                 'ધ',
                 'ન',
                 'પ',
                 'ફ',
                 'બ',
                 'ભ',
                 'મ',
                 'ય',
                 'ર',
                 'લ',
                 'ળ',
                 'વ',
                 'શ',
                 'ષ',
                 'સ',
                 'હ']

ka_single_cons = ['ಕ',
                             'ಖ',
                             'ಗ',
                             'ಘ',
                             'ಙ',
                             'ಚ',
                             'ಛ',
                             'ಜ',
                             'ಝ',
                             'ಞ',
                             'ಟ',
                             'ಠ',
                             'ಡ',
                             'ಢ',
                             'ಣ',
                             'ತ',
                             'ಥ',
                             'ದ',
                             'ಧ',
                             'ನ',
                             'ಪ',
                             'ಫ',
                             'ಬ',
                             'ಭ',
                             'ಮ',
                             'ಯ',
                             'ರ',
                             'ಱ',
                             'ಲ',
                             'ವ',
                             'ಶ',
                             'ಷ',
                             'ಸ',
                             'ಹ',
                             'ಳ',
                             'ೞ']


ory_single_cons = ['କ',
                                                                             'ଖ',
                                                                             'ଗ',
                                                                             'ଘ',
                                                                             'ଙ',
                                                                             'ଚ',
                                                                             'ଛ',
                                                                             'ଜ',
                                                                             'ଝ',
                                                                             'ଞ',
                                                                             'ଟ',
                                                                             'ଠ',
                                                                             'ଡ',
                                                                             'ଢ',
                                                                             'ଣ',
                                                                             'ତ',
                                                                             'ଥ',
                                                                             'ଦ',
                                                                             'ଧ',
                                                                             'ନ',
                                                                             'ପ',
                                                                             'ଫ',
                                                                             'ବ',
                                                                             'ଵ',
                                                                             'ଭ',
                                                                             'ମ',
                                                                             'ଯ',
                                                                             'ୟ',
                                                                             'ର',
                                                                             'ଲ',
                                                                             'ଳ',
                                                                             'ୱ',
                                                                             'ଶ',
                                                                             'ଷ',
                                                                             'ସ',
                                                                             'ହ']

pa_single_cons = ['ਕ',
                                 'ਖ',
                                 'ਗ',
                                 'ਘ',
                                 'ਙ',
                                 'ਚ',
                                 'ਛ',
                                 'ਜ',
                                 'ਝ',
                                 'ਞ',
                                 'ਟ',
                                 'ਠ',
                                 'ਡ',
                                 'ਢ',
                                 'ਣ',
                                 'ਤ',
                                 'ਥ',
                                 'ਦ',
                                 'ਧ',
                                 'ਨ',
                                 'ਪ',
                                 'ਫ',
                                 'ਬ',
                                 'ਭ',
                                 'ਮ',
                                 'ਯ',
                                 'ਰ',
                                 'ਲ',
                                 'ਵ',
                                 'ੜ',
                                 'ਸ',
                                 'ਹ']

ory_2_eng_phonetics ={'A': [''], # For Satya
                     'B': [''],
                     'C': [''],
                     'D': [''],
                     'E': [''],
                     'F': [''],
                     'G': [''],
                     'H': [''],
                     'I': [''],
                     'J': [''],
                     'K': [''],
                     'L': [''],
                     'M': [''],
                     'N': [''],
                     'O': [''],
                     'P': [''],
                     'Q': [''],
                     'R': [''],
                     'S': [''],
                     'T': [''],
                     'U': [''],
                     'V': [''],
                     'W': [''],
                     'X': [''],
                     'Y': [''],
                     'Z': [''],}


hi_mr_2_en_phonetics =  {'A': ['ए','ऐ' ],# Is Marathi the same?  # checked by Faheem
                         'B': ['बी',],
                         'C': ['सी',],
                         'D': ['डी',],
                         'E': ['ई',],
                         'F': ['ऐफ', 'एफ' ],
                         'G': ['जी',],
                         'H': ['ऐच', 'एच' ],
                         'I': ['आइ',],
                         'J': ['जे',],
                         'K': ['के',],
                         'L': ['ऐल', 'एल' ],
                         'M': ['ऐम', 'एम' ],
                         'N': ['ऐन', 'एन' ],
                         'O': ['ओ',],
                         'P': ['पी',],
                         'Q': ['क्यू',],
                         'R': ['आर',],
                         'S': ['ऐस', 'एस' ],
                         'T': ['टी',],
                         'U': ['यू',],
                         'V': ['वी',],
                         'W': ['डब्ल्यू',],
                         'X': ['ऐक्स', 'एक्स' ],
                         'Y': ['वाय', 'वाई'],
                         'Z': ['ज़ैड' ],}


ta_2_eng_phonetics= { 'A': ['ஏ',],  #from wikipedia
                        'B': ['பீ',],
                        'C': ['சீ',],
                        'D': ['டீ',],
                        'E': ['ஈ',],
                        'F': ['எஃப்',],
                        'G': ['ஜீ',],
                        'H': ['எச்', 'ஹெச்',],
                        'I': ['ஐ',],
                        'J': ['ஜே', 'ஜை',],
                        'K': ['கே',],
                        'L': ['எல்',],
                        'M': ['எம்',],
                        'N': ['என்',],
                        'O': ['ஓ',],
                        'P': ['ப்பீ',],
                        'Q': ['கியூ',],
                        'R': ['ஆர்',],
                        'S': ['எஸ்',],
                        'T': ['ட்டீ',],
                        'U': ['யூ',],
                        'V': ['வீ',],
                        'W': ['டபிள்-யூ',],
                        'X': ['எக்ஸ்',],
                        'Y': ['வை',],
                        'Z': ['செட்',], }



bn_asm_mni_2_eng_phonetics = {'A':['এ',],  # FROM https://bn.switch-case.com/51494160 and google translate 
                             'B':['বি',],
                             'C':['সি',],
                             'D':['ডি',],
                             'E':['ই',],
                             'F':['এফ',],
                             'G':['জি',],
                             'H':['এইচ',],
                             'I':['আম'],
                             'J': ['জে',],
                             'K':['কে',],
                             'L':['এল',],
                             'M':['এম',],
                             'N':['এন',],
                             'O':['হে',],
                             'P':['পি',],
                             'Q':['কিউ',],
                             'R':['আর',],
                             'S':['এস',],
                             'T':['টি',],
                             'U':['ইউ',],
                             'V':['ভি ',],
                             'W':['ডব্লু',],
                             'X':['এক্স',],
                             'Y':['ওয়াই',],
                             'Z':['জেড', ]  }


pa_2_eng_phonetics = {'A':['ਏ',],  # FROM http://englishsikhowithpunjabi.blogspot.com/2017/08/an-introduction-to-alphabet-in-english.html
                     'B':['ਬੀ',],
                     'C':['ਸੀ',],
                     'D':['ਡੀ',],
                    'E':['ਈ',],
                     'F':['ਐੱਫ',],
                     'G':['ਜੀ',],
                     'H':['ਐਚ',],
                     'I':['ਆਈ',],
                     'J': ['ਜੇ',],
                     'K':['ਕੇ',],
                     'L':['ਐਲ',],
                     'M':['ਐੱਮ',],
                     'N':['ਐੱਨ',],
                     'O':['ਓ',],
                     'P':['ਪੀ',],
                     'Q':['ਕੀਓ',],
                     'R':['ਆਰ',],
                     'S':['ਐੱਸ', 'ਸ'],
                     'T':['ਟੀ',],
                     'U':['ਯੂ',],
                     'V':['ਵੀ',],
                     'W':['ਡਬਲਿਊ',],
                     'X':['ਐਕ੍ਸ',],
                     'Y':['ਵਾਈ',],
                     'Z':['ਜ਼ੈਡ',],}



kn_2_eng_phonetics = {'A':['ಎ'], # from google translate
                     'B':['ಬಿ',],
                     'C':['ಸಿ',],
                     'D':['ಡಿ',],
                    'E':['ಇ',],
                     'F':['ಎಫ್',],
                     'G':['ಜಿ',],
                     'H':['ಹೆಚ್', 'ಎಚ್‌'],
                     'I':['ಐ',],
                     'J': ['ಜೆ',],
                     'K':['ಕೆ',],
                     'L':['ಎಲ್',],
                     'M':['ಎಂ',],
                     'N':['ಎನ್',],
                     'O':['ಒ',],
                     'P':['ಪಿ',],
                     'Q':['ಕ್ಯೂ',],
                     'R':['ಆರ್',],
                     'S':['ಎಸ್'],
                     'T':['ಟಿ',],
                     'U':['ಯು',],
                     'V':['ವಿ',],
                     'W':['ಡಬ್ಲ್ಯೂ',],
                     'X':['ಎಕ್ಸ್',],
                     'Y':['ವೈ',],
                     'Z':['ಜೆಡ್',], }


UN = {'ta' : 'ஐநா' }



te_2_eng_phonetics = {'A':['ఎ'], # from google translate but checked by https://books.google.co.uk/books?id=YdMoDwAAQBAJ&pg=PA37&lpg=PA37&dq=%E0%B0%8E+%E0%B0%AC%E0%B0%BF+%E0%B0%B8%E0%B0%BF+%E0%B0%A1%E0%B0%BF+%E0%B0%87+%E0%B0%8E%E0%B0%AB%E0%B1%8D+%E0%B0%9C%E0%B0%BF+%E0%B0%B9%E0%B1%86%E0%B0%9A%E0%B1%8D+alphabet+english&source=bl&ots=8pbIJgmTJh&sig=ACfU3U2nkc0BoYJxr7AnCkQruQq1RC1LuQ&hl=en&sa=X&ved=2ahUKEwj_o7bd3KPlAhXUbMAKHTuLBlkQ6AEwBHoECAUQAQ#v=onepage&q=%E0%B0%8E%20%E0%B0%AC%E0%B0%BF%20%E0%B0%B8%E0%B0%BF%20%E0%B0%A1%E0%B0%BF%20%E0%B0%87%20%E0%B0%8E%E0%B0%AB%E0%B1%8D%20%E0%B0%9C%E0%B0%BF%20%E0%B0%B9%E0%B1%86%E0%B0%9A%E0%B1%8D%20alphabet%20english&f=false
                     'B':['బి',],
                     'C':['సి',],
                     'D':['డి',],
                    'E':['ఇ',],
                     'F':['ఎఫ్',],
                     'G':['జి',],
                     'H':['హెచ్‌'],
                     'I':['ఐ',],
                     'J': ['జె',],
                     'K':['కె',],
                     'L':['ఎల్',],
                     'M':['ఎం', 'ఎమ్',],
                     'N':['ఎన్',],
                     'O':['ఓ',],
                     'P':['పి',],
                     'Q':['క్యూ',],
                     'R':['ఆర్',],
                     'S':['ఎస్'],
                     'T':['టి',],
                     'U':['యు',],
                     'V':['వి',],
                     'W':['డబ్ల్యూ',],
                     'X':['ఎక్స్',],
                     'Y':['వై',],
                     'Z':['జెడ్',],}


ml_2_eng_phonetics ={'A': ['എ'],  # from google translate and  http://pandajama.ru/ml/deti/english-alphabet-and-its-pronunciation-in-russian-alphabet-in-english.html
                     'B': ['ബി'],
                     'C': ['സി'],
                     'D': ['ഡി'],
                     'E': ['ഇ'],
                     'F': ['എഫ്'],
                     'G': ['ജി'],
                     'H': ['എച്ച്'],
                     'I': ['ഐ'],
                     'J': ['ജെ'],
                     'K': ['കെ'],
                     'L': ['എൽ'],
                     'M': ['എം'],
                     'N': ['എൻ'],
                     'O': ['ഒ'],
                     'P': ['പി '],
                     'Q': ['ക്യൂ'],
                     'R': ['ആർ'],
                     'S': ['എസ്'],
                     'T': ['ടി'],
                     'U': ['യു'],
                     'V': ['വി'],
                     'W': ['ഡബ്ല്യു'],
                     'X': ['എക്സ്'],
                     'Y': ['വൈ'],
                     'Z': ['സെഡ്'],}




gu_2_eng_phonetics = {'A':['એ',], # checked by Faheem
                     'B':['બી',],
                     'C':['સી',],
                     'D':['ડી',],
                    'E':['ઇ',],
                     'F':['એફ',],
                     'G':['જી',],
                     'H':['એચ',],
                     'I':['આઈ',],
                     'J': ['જે',],
                     'K':['કે',],
                     'L':['એલ',],
                     'M':['એમ',],
                     'N':['એન',],
                     'O':['ઓ',],
                     'P':['પી',],
                     'Q':['ક્યૂ',],
                     'R':['આર',],
                     'S':['એસ',],
                     'T':['ટી',],
                     'U':['યુ',],
                     'V':['વી',],
                     'W':['ડબલ્યુ',],
                     'X':['એક્સ',],
                     'Y':['વાય',],
                     'Z':['ઝેડ',], }
                    





PROF = {'pa': 'ਪ੍ਰੋ'}



phonetics = {"hi" : hi_mr_2_en_phonetics,
             "mr" : hi_mr_2_en_phonetics,
             "ory" : ory_2_eng_phonetics,
             "ta" : ta_2_eng_phonetics,
             "bn" : bn_asm_mni_2_eng_phonetics,
             "asm" : bn_asm_mni_2_eng_phonetics,
             "mni" : bn_asm_mni_2_eng_phonetics,
             "pa" : pa_2_eng_phonetics,
             "kn" : kn_2_eng_phonetics,
             "te" : te_2_eng_phonetics,
             "ml" : ml_2_eng_phonetics,
             "gu" : gu_2_eng_phonetics,
             }
cons = {"hi" :  hi_mr_single_cons,
       "mr" : hi_mr_single_cons,
       "gu" : gu_single_cons,
       "ka" : ka_single_cons,
       "ory" : ory_single_cons,
       "pa" : pa_single_cons}

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
LANGS = ["asm", "bn", "gu", "hi", "kn", "ml", "mni", "mr", "ory", "pa", "ta", "te"]

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
        nbps = excepts.get(lang,[])
        if nbps:
          for nbp in nbps:
            print("# " + key, file=ofh)
            print(nbp, file=ofh)
      print(file=ofh)

      print("#others", file=ofh)
      for nbp in others.get(lang, []):
        print(nbp, file=ofh)
      print(file=ofh)

      print("#phonetics", file=ofh)
      for key,nbps in sorted(phonetics.get(lang,{}).items()):
        print("# " + key, file=ofh)
        for nbp in nbps:
          print(nbp, file=ofh)
      print(file=ofh)

      print("#consonants", file=ofh)
      for c in cons.get(lang, []):
        print(c, file=ofh)
      print(file=ofh)


if __name__ == "__main__":
  main()



