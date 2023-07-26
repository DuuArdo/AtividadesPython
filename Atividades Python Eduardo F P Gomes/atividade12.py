def calcular_peso_ideal_altura(sexo, altura):
    if sexo == 'M' or sexo == 'm':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F' or sexo == 'f':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Use 'M' ou 'F'.")

    return peso_ideal

def main():
    try:
        sexo = input("Digite 'M' para masculino ou 'F' para feminino: ")
        altura = float(input("Digite sua altura em metros: "))
        peso_ideal = calcular_peso_ideal_altura(sexo, altura)
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
