"""

>>> passay.make_letter(generator, passay.LetterType.VOWEL, False, False, choice)[0]
'a'

>>> passay.make_letter(generator, passay.LetterType.CONSONANT, False, False, choice)[0]
'b'

>>> passay.make_letter(generator, passay.LetterType.VOWEL, False, False, new_random())[0]
'u'

>>> passay.make_letter(generator, passay.LetterType.CONSONANT, False, False, new_random())[0]
't'

>>> passay.make_word(generator, 5, choice)
'babab'

>>> passay.make_word(generator, 5, new_random())
'oleni'

"""

import passay
import random

VOWELS = 'aeiou'
CONSONANTS = 'bdfgklmnprstvz'
TERMINAL_PUNCTUATION = ['.', '...', '!', '?', '!!', '!?', '?!', '??']

generator = passay.PasswordGenerator(
  words=[6, 8],
  vowels=VOWELS,
  consonants=CONSONANTS,
  punctuation=TERMINAL_PUNCTUATION,
  pairs=None,
  numbers=0,
  word_start=passay.LetterType.BOTH,
  separator=' ',
  capitalize=passay.Capitalize.FIRST,
  bad=None)

def choice(x):
  for i in x:
    return i

def new_random():
  random.seed(0)
  return random.choice
