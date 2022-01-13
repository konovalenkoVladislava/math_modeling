
def lez_funk(L):
  S=0
  for i in range (len(L)):
    S=S+L[i]
  return S/len(L)

L=[1,4,4,10]
print(lez_funk(L))