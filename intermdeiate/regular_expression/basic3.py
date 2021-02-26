import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence = 'Start a sentence and then bring it to an end'


# This matches all the phonenumbers present in in the text_to_search
# phonenumber_pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# . matches any character set but we want it to match only - and .
# phonenumber_pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')

# Matches 800 and 900
phonenumber_pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')

phonenumber_matches = phonenumber_pattern.finditer(text_to_search)

for phonenumber in phonenumber_matches:
    print(phonenumber)

# Range Matches
# Pattern matching from a to z
# range_pattern = re.compile(r'[a-z]')

# Pattern Matching from 1 to 9
# range_pattern = re.compile(r'[1-9]')

# Pattern matches with quantifiers
# This matches exact 3 digits of numbers
range_pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
range_matches = range_pattern.finditer(text_to_search)

for range in range_matches:
    print(range)
