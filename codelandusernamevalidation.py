import re

def CodelandUsernameValidation(strParam):

  if len(strParam) < 4 or len(strParam) > 25:
    return "false"

  if not strParam[0].isalpha():
    return "false"

  for char in strParam:
    if not (char.isalnum() or char == '_'):
      return "false"

  if strParam[-1] == '_':
    return "false"

  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))