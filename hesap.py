def topla():
  x=int(input("Toplamak için1.sayı:"))
  y=int(input("Toplamak için2.sayı:"))
  print(x,"+",y,"=,x+y")

def cikar(x,y):
  b=x-y
  return b
def carp(x,y):
  c=x*y
  return print(c)
def bol(x,y):
  d=x/y
  return print(d)
x=float(input("1.sayı"))
y=float(input("2.sayı")) 
islem=input("Yapmak istediğin islem:+ , -,* , / :")
if islem == "+":
  print (topla(x,y))
elif islem=="-":
  print(cikar(x,y))
elif islem == "*":
  print (carp(x,y))
elif islem == "/":
  print (bol(x,y))
else  :
  print("Yanlıs islem")


