from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Calculadora Open Source")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar Avanzada")
    print("6. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", sumar(a, b))
    elif opcion == '2':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", restar(a, b))
    elif opcion == '3':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicar(a, b))
    elif opcion == '4':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", dividir(a, b))
    elif opcion == '5':
        numeros = list(map(float, input("Ingresa los números separados por espacio: ").split()))
        print("Resultado:", suma_avanzada(numeros))
    elif opcion == '6':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
