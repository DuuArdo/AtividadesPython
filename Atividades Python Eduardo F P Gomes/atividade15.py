import math

def calcular_quantidade_latas(area):
    cobertura_por_lata = 18 * 3  # 18 litros de tinta cobrem 54 metros quadrados (18 * 3)
    quantidade_latas = math.ceil(area / cobertura_por_lata)
    return quantidade_latas

def calcular_preco_total(quantidade_latas, preco_por_lata):
    return quantidade_latas * preco_por_lata

def main():
    try:
        preco_por_lata = 80.00  # Preço de uma lata de tinta (18 litros)
        area_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

        quantidade_latas = calcular_quantidade_latas(area_pintada)
        preco_total = calcular_preco_total(quantidade_latas, preco_por_lata)

        print(f"\nQuantidade de latas de tinta a serem compradas: {quantidade_latas}")
        print(f"Preço total: R$ {preco_total:.2f}")

    except ValueError:
        print("Por favor, digite um valor numérico válido para a área.")

if __name__ == "__main__":
    main()
