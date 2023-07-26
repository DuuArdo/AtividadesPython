def calcular_excesso_multa(peso):
    limite_peso = 50  # Limite estabelecido pelo regulamento (50 quilos)
    excesso = max(0, peso - limite_peso)  # Calcula o excesso, se houver
    multa_por_quilo = 4.00  # Valor da multa por quilo excedente
    multa = excesso * multa_por_quilo  # Calcula o valor total da multa
    return excesso, multa

def main():
    try:
        peso_peixes = float(input("Digite o peso de peixes trazido por João (em quilos): "))
        excesso, multa = calcular_excesso_multa(peso_peixes)

        if excesso > 0:
            print(f"João excedeu o limite de pesca em {excesso:.2f} quilos.")
            print(f"João deverá pagar uma multa de R$ {multa:.2f}.")
        else:
            print("João não excedeu o limite de pesca. Nenhuma multa é devida.")
    except ValueError:
        print("Por favor, digite um valor numérico válido para o peso.")

if __name__ == "__main__":
    main()
