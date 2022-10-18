i=0
a=[]
while True : 
    numeroIngresado = input() 
    i += 1
    if (numeroIngresado[0] == '-'): 
        #Aqui determina si es negativo
        #i = cantidadNumeros + 1 # Con esto se sale y no convierte ningun numero
        #print()
        break
    else:
        try:  
            if (numeroIngresado[0] == '0' and numeroIngresado[1] == 'x'): # Aqui es hexadecimal
               # print( int(numeroIngresado,16))
               e=int(numeroIngresado,16)
            else: # Aqui es decimal
               e=(hex(int(numeroIngresado))).upper().replace("X","x")
        except:
            e=int(hex(int(numeroIngresado)))# En esta linea implementa la misma
            #que en la convercion decimal de la liena 15, para poder tomar el caso del 0 y el 0x0 
    a.append(e)        
for i in a:
    print(i)