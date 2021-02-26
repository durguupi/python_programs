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


# This matches all the digits present in in the text_to_search
pattern_num = re.compile(r'\d')
matches_num = pattern_num.finditer(text_to_search)

for num in matches_num:
    print(num)
print("===========Space Matching==================")
# This matches all the spaces,tan,newline present in in the text_to_search
pattern_space = re.compile(r'\s')
matches_space = pattern_space.finditer(text_to_search)

for space in matches_space:
    print(space)


print("===========Word boundary==================")
# This matches all the words Ha starting and not words with ha in the middle
pattern_word = re.compile(r'\bHa')
matches_word = pattern_word.finditer(text_to_search)

for word in matches_word:
    print(word)
