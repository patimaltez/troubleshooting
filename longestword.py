import re

def LongestWord(sen):

  sen = re.sub(r'[^\w\s]', '', sen)
  words = sen.split()
  longest_word = ''
  max_length = 0

  for word in words:
    if len(word) > max_length:
      max_length = len(word)
      longest_word = word
  
  return longest_word

# keep this function call here 
print(LongestWord(input()))