def FirstFactorial(num):
    if isinstance(num, int) and num >= 0:
        if num == 0:
            return 1
        else:
            result = 1
            # Iterate from 2 to n (inclusive) and multiply each number to result
            for i in range(2, num + 1):
                result *= i
            # Return the final result
            return result
    else:
        return None
pass

# keep this function call here 
print(FirstFactorial(input()))

''' 
#Another solution
def FirstFactorial(num):

  if num == 0 or num == 1:
    return 1
  else:
    return num * FirstFactorial(num - 1)

# keep this function call here 
print(FirstFactorial(input()))
'''