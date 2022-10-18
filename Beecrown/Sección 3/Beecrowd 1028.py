movientos = int(input())
def mcd (a,b):
  if b>a:a,b=b,a 
  while a%b!=0:  
    b,a=a%b,b  
  return b  
for i in range (movientos):
  cartas = input().split()
  carta = int(cartas[0])
  carta2= int(cartas[1])
  print(mcd(carta,carta2))
  




  




