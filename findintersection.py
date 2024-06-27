def FindIntersection(strArr):

  lista1 = list(map(int, strArr[0].split(',')))
  lista2 = list(map(int, strArr[1].split(',')))
  intersecao = []
  i = 0
  j = 0

  while i < len(lista1) and j < len(lista2):
    if lista1[i] == lista2[j]:
      intersecao.append(lista1[i])
      i += 1
      j += 1
    elif lista1[i] < lista2[j]:
      i += 1
    else:
      j += 1
  if not intersecao:
    return "false"
  else:
    return ','.join(map(str, intersecao))

# keep this function call here 
print(FindIntersection(input()))