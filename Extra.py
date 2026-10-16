op=""

while op!=0:
    #los 5 ejercicios que se hicieron en clase
    print("""
    1. Saludar
    2. Calcular edad en el año 2030     
    3. Operaciones matematicas
    4. Par o impar
    5. Aprobar o reprobar


    0. Salir
    """)
    op=int(input("Ingrese una opcion:  "))

    if op==1:
        nombre=input("Ingrese su nombre:  ")
        print(f"Hola {nombre} como estas?")
    elif op==2:
        nacimiento=int(input("Ingrese su año de nacimineto: "))
        print(f"Usted tendra {2030-nacimiento} en el año 2030")
    elif op==3:
        num1=int(input("Ingrese el primer numero:  "))
        num2=int(input("Ingrese el segundo numero:  "))

        print(f"""

        La suma de {num1} + {num2} = {num1+num2}
        La resta de {num1} - {num2} = {num1-num2}
        La multiplicacion de {num1} x {num2} = {num1*num2}
        """)
        if num2 != 0:
            print(f"La division de {num1} / {num2} = {num1/num2}")
        else:
            print("No se puede dividir entre 0")

    elif op==4:
        num=int(input("Ingrese un numero:  "))
        if num%2==0:
            print(f"El numero {num} es par")
        else:
            print(f"El numero {num} es impar")

    elif op==5:
        nota=int(input("Ingrese su nota:  "))

        if nota>1 and nota<=100:
            if nota >=51:
                print(f"Su nota es {nota} y ha aprobado")
            else:
                print(f"Su nota es {nota} y ha reprobado")
        else:
            print("Ingrese una nota valida")

    elif op==0:
        print("Saliendo del sistema...")