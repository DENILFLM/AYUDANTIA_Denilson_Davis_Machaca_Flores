nota=int(input("Ingrese su nota:  "))

if nota>1 and nota<=100:
    if nota >=51:
        print(f"Su nota es {nota} y ha aprobado")
    else:
        print(f"Su nota es {nota} y ha reprobado")
else:
    print("Ingrese una nota valida")