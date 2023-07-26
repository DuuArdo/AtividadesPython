def calcular_tempo_download(tamanho_arquivo, velocidade_link):
    tempo_min = (tamanho_arquivo / velocidade_link) * 8
    return tempo_min

def main():
    try:
        tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
        velocidade_link = float(input("Digite a velocidade do link de Internet (em Mbps): "))

        tempo_download_min = calcular_tempo_download(tamanho_arquivo, velocidade_link)

        print(f"Tempo aproximado de download: {tempo_download_min:.2f} minutos")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()
