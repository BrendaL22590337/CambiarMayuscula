# convertir_mayuscula.py

def primera_mayuscula(texto):
    # Convierte la primera letra de cada palabra a mayúscula
    return texto.title()


# Programa principal
def main():
    texto = input("Escribe una frase: ")
    resultado = primera_mayuscula(texto)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
