def calculadora():
    operacion = input("¿Qué operación quieres hacer? Escribe una de Las operaciones posibles \n-suma\n-resta\n-potencia\n-division\n")
    num1 = float(input("Introduce el primer valor: "))
    num2 = float(input("Introduce el segundo valor: "))
    if(operacion == "suma"):
        print(num1 + num2) 
    elif(operacion == "resta"):
        print(num1 - num2) 
    elif(operacion == "potencia"):
        print(num1**num2)
    elif (operacion == "division"):
        print(num1 / num2) 
    else:
        print("Operación errónea. Indica una de Las operaciones posibles:\n-suma\n-resta\n-potencia\n")

calculadora()