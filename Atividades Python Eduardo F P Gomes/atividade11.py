def calcular_peso_ideal_altura(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

def main():
    try:
        altura = float(input("Digite sua altura em metros: "))
        peso_ideal = calcular_peso_ideal_altura(altura)
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    main()
