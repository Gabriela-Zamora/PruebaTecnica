def palindromo(g):
    
    g=' '.join(filter(str.isalnum, g)).lower()
    return g == g[::-1]

palabra=input("introduce una secuencia de caracteres: ")
if palindromo(palabra):
    print(f"la palabra '{palabra}' es verdadero.")
else:
    print(f"la palabra '{palabra}' es falso.")