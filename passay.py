from collections import namedtuple

import random

import badwords
from Enum import Enum

PasswordGenerator = namedtuple(
  'PasswordGenerator',
  ['words', 'vowels', 'consonants', 'pairs', 'punctuation', 'numbers',
   'word_start', 'separator', 'capitalize', 'bad'])

Capitalize = Enum('NONE', 'FIRST', 'WORDS')
LetterType = Enum('CONSONANT', 'VOWEL', 'BOTH')

Pairs = namedtuple('Pairs', ['initial', 'middle', 'terminal'])
Bad = namedtuple('Bad', ['initial', 'terminal'])

NUMBERS = '0123456789'

def make_word(generator, length, choice=random.choice):
  while True:
    parts = []
    letter_type = generator.word_start
    if letter_type is LetterType.BOTH:
      letter_type = choice([LetterType.CONSONANT, LetterType.VOWEL])

    for i in xrange(length):
      if letter_type is LetterType.CONSONANT:
        letters = generator.consonants
        if not i:
          letters += generator.pairs.initial
        elif i == (length - 1):
          letters += generator.pairs.terminal
        else:
          letters += generator.pairs.middle
        letter_type = LetterType.VOWEL
      else:
        letters = generator.vowels
        letter_type = LetterType.CONSONANT
      parts.append(choice(letters))

    word = ''.join(parts)
    if not badwords.is_bad(word):
      return word

def make_password(generator, choice=random.choice):
  words = [make_word(generator, w, choice) for w in generator.words]
  if generator.capitalize is Capitalize.FIRST:
    if words:
      words[0] = words[0].capitalize()
  elif generator.capitalize is Capitalize.WORDS:
    words = [w.capitalize() for w in words]
  if generator.numbers:
    word = ''.join(choice(NUMBERS) for i in xrange(generator.numbers))
    words.append(word)
  result = generator.separator.join(words)
  return result + choice(generator.punctuation)
