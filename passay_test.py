"""

>>> passay.make_letter(generator, passay.LetterType.VOWEL, False, False, choice)[0]
'a'

>>> passay.make_letter(generator, passay.LetterType.CONSONANT, False, False, choice)[0]
'b'

"""

import passay

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
