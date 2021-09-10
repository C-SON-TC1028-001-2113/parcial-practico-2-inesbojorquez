

def main():
    #escribe tu código abajo de esta línea
    #Iniciar con una variable igual a 1, checar si la variable al cuadrado es mayor que N, 
    # si no lo es, entonces incrementar la variable y repetir.
    n = int(input("Escribe un numero : "))
    r = 1
    while n >=r**2:
        r = r+1
    print(r)                

if __name__=='__main__':
    main()
