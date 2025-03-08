#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones 
#múltiplos de n, y muestre por pantalla la lista resultante
#Entrada:Una lista con el abecedario un numero n
#Salida:Una lista de salida donde solamente se encuentren las letras que no ocupan posiciones multipolos de n

def abecedario():
     lista = ['a','b','c','d','e','f','g','h','i','j',
       'k','l','m','n','ñ','o','p','q','r','s',
       't','u','v','w','x','y','z']
     
     print("Ingresel el numero")
     Numero = int(input())
     salida = [lista.pop(i-1) for i in range(len(lista), 1, -1) if i % Numero == 0]
     print(salida)

abecedario()