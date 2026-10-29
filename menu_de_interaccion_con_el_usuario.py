
#Menu de presentación.
def mostrar_menu():
    print("\n" + "*" *40)
    print("Sistema Comercial de Stock/Comrpa/Venta de Lanas")
    print("*" *40)
    print("1. Ingreso de Mercadería")
    print("2. Venta de Mercadería")
    print("3. Ocupar Cupo de Clases de Tejido")
    print("4. Liberar Cupo de Clases de Tejido")
    print("0. Salir del programa")

#Función del menú principal.
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ").strip

        if opcion == "1":
            ingresar_mercaderia()
        elif opcion == "2":
            vender_mercaderia()
        elif opcion == "3":
            cupo_clases_vendido()
        elif opcion == "4":
            cupo_clases_liberado()
        elif opcion == "0":
            print("Adiós!")
            break
        else: 
            print("Opción inválida. Vuelva a intentar.")

#Ejecutar menú automático.
if __name__ == "__main__":
    main()


