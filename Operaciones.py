op = int(input("elige una opcion: \n 1.-Sumatoria \n 2.-Factorizacion \n 3.-Maximo comun divisor de dos numeros\n 4.-Potencia de un numero\n 5.-Serie fibonacci\n"))
if (op==1):
    print("1.-Sumatroria de un numero")
#sumatoria
    def sumatoria(num):
        if num==1:
            return 1
        else:
            return num+sumatoria(num-1)
    num = int(input("Ingrese un número de la sumatoria: "))
    print(sumatoria(num))
if(op==2):
    print("2.-factorial  de un numero:")
        #factorial
    def facto(n):
        if n==1:
            return 1
        else:
            return n*facto(n-1)
    n = int(input("Ingrese el numero del factorial: "))
    print(facto(n))
if(op==3):
    print("3.-Maximo comun divisor de dos numeros:")
    #maximo comun divisor
    def mcd(a,b):
        minimo =min(a,b)
        maximo=max(a,b)

        if minimo==0:
            return maximo
        elif minimo==1:
            return 1
        else:
            return mcd(minimo,maximo%minimo)
    
    a = int(input("Ingrese un numero: "))
    b= int(input("Ingrese el otro numero: "))
    print("el maximo comun divisor es: "+ str (mcd(a,b)))
if(op==4):
    print("4.- Potencia de un numero:")
#potencia de un numero
    def potencia(z,y):
        if (y==0):
            return 1
        elif(z==0):
            return 0
        elif(y==1):
            return z
        else:
            return z *potencia(z,y -1)

    z = int(input("Ingrese un número: "))
    y = int(input("Ingrese la potencia: "))
    print(potencia(z,y))
if (op==5):
    print("5.- Serie fibonacci de un numero:")
#serie fibonaci de un numero
    def fibonacci(nume):
        if (nume == 1):
            return(0)
        elif(nume == 2):
            return(1)
        elif(nume > 2):
            return(fibonacci(nume - 1) + fibonacci(nume - 2))


    while True:
        nume = int(input("Ingrese un número: "))
        if (nume>=1):
            break
    for i in range(nume):
        print(fibonacci(i))


