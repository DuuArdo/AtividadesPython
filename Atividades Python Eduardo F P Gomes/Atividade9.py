def celsius_Pra_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_Pra_fahrenheit(celsius)
        print(f"{celsius:.2f} graus celsius São {fahrenheit:.2f} graus em Fahrenheit.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    main()
