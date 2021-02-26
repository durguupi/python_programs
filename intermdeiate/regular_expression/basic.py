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
# This Prints with tab space in it since we have \t
print("\ttab")
# Now if we want the \t also to be considered as output.we pass r in it which means raw output
print(r"\ttab")

# Compile method will alow us to seperate our patterns to variable and use tha tvariable to perform mutiple searches
pattern = re.compile(r'abc')
matches_text = pattern.finditer(text_to_search)

# It displays the beginning and end of the index of the pattern span(1,4)
for match in matches_text:
    print(match)
# From the output of abc we got the index and then now it prints those values
print(text_to_search[1:4])

# For special characters we have to us \ before that
pattern_url = re.compile(r'coreyms\.com')
matches_url = pattern_url.finditer(text_to_search)

for url in matches_url:
    print(url)

# This matches the number present in the text_to_search
pattern_num = re.compile(r'555')
matches_num = pattern_num.finditer(text_to_search)

for num in matches_num:
    print(num)
