def main():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        num3 = float(input("Digite o número real: "))

        # Cálculo: produto dobro do primeiro com metade do segundo
        produto_dobro = (2 * num1) * (num2 / 2)
        print(f"O produto dobro do primeiro com metade do segundo é: {produto_dobro}")

        # Cálculo: soma do triplo do primeiro com o terceiro
        soma_triplo = (3 * num1) + num3
        print(f"A soma do triplo do primeiro com o terceiro é: {soma_triplo}")

        # Cálculo: terceiro ao cubo
        cubo_terceiro = num3 ** 3
        print(f"O terceiro ao cubo é: {cubo_terceiro}")
        
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()
