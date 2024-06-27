def MinWindowSubstring(strArr):

  N, K = strArr
  target_counts = {char:K.count(char) for char in set(K)}
  window_counts = {char: 0 for char in set(K)}

  min_window =""
  min_length = float('inf')
  left, right = 0, 0

  def contains_all(window_counts,target_counts):
    for char in target_counts:
      if window_counts[char] < target_counts[char]:
        return False
    return True
  while right < len(N):
    if N[right] in window_counts:
      window_counts[N[right]] += 1
    while contains_all(window_counts,target_counts):
      if right - left + 1 < min_length:
        min_length = right - left + 1
        min_window = N[left:right+1]
      if N[left] in window_counts:
        window_counts[N[left]] -= 1

      left += 1
    right += 1
  return min_window

# keep this function call here 
print(MinWindowSubstring(input()))