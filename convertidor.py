import temperatura
import masa
import tiempo
def main():
    while True:

        print("Menú Principal:")
        print("[1] Calcular Celsius a Fahrenheit")
        print("[2] Calcular Celsius a Kelvin")
        print("[3] Calcular Fahrenheit a Celsius")
        print("[4] Calcular Fahrenheit a Kelvin")
        print("[5] Calcular Kelvin a Celsius")
        print("[6] Calcular Kelvin a Fahrenheit")
        print("[7] Calcular Kilogramos (kg) a Gramos (g)")
        print("[8] Calcular Kilogramos (kg) Toneladas (t)")
        print("[9] Calcular Gramos (g) a Kilogramos (kg)")
        print("[10] Calcular Gramos (g) a Toneladas (t)")
        print("[11] Calcular Toneladas (t) a Kilogramos (kg)")
        print("[12] Calcular Toneladas (t) a Gramos (g)")
        print("[13] Calcular Segundos a Minutos")
        print("[14] Calcular Segundos a Horas ")
        print("[15] Calcular Minutos a Segundos ")
        print("[16] Calcular Minutos a Horas ")
        print("[17] Calcular Horas a Segundos  ")
        print("[18] Calcular Horas a Minutos ")
        
        print("[0] Salir")
        
        opcion = input("Ingrese una opción: ")
        valor_inicial=int(input("ingrese valor inicial: "))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resultado = temperatura.celsius_a_fahrenheit(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 2:
                resultado = temperatura.celsius_a_kelvin(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 3:
                resultado = temperatura.fahrenheit_a_celsius(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 4:
                resultado = temperatura.fahrenheit_a_kelvin(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 5:
                resultado = temperatura.kelvin_a_celsius(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 6:
                resultado = temperatura.kelvin_a_fahrenheit(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 7:
                resultado = masa.Kilogramos_a_Gramos (valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 8:
                resultado = masa.Kilogramos_a_Toneladas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 9:
                resultado = masa.gramos_a_kilogramos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 10:
                resultado = masa.gramos_a_toneladas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 11:
                resultado = masa.tonelada_a_kilogramos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 12:
                resultado = masa.tonelada_a_gramos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 13:
                resultado = tiempo.segundos_a_Minutos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 14:
                resultado = tiempo.Segundos_a_Horas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 15:
                resultado = tiempo.Minutos_a_Segundos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 16:
                resultado = tiempo.Minutos_a_Horas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 17:
                resultado = tiempo.Horas_a_Segundos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 18:
                resultado = tiempo.Horas_a_Minutos(valor_inicial)
                print("el resultado es: ", resultado)

                
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()

