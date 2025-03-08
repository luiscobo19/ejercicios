#Dada una frase averiguar cuantas vocales tiene y mostrarlas. 
# Para esto, se debe usar la siguiente lista vowels =['a', 'e', 'i', 'o', 'u']

frase = input("ingrese una frase")
def Bucar_Vocales(frase):
    vowels =['a', 'e', 'i', 'o', 'u']
    Buscar=[letras for letras in frase if letras in vowels]
    print("vocales",Buscar)
    print("Numero de Vocales", len(Buscar))

Bucar_Vocales(frase)  