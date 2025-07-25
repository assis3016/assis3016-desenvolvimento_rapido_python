import os
import shutil

def mover_jpgs_selecionados(diretorio_origem, diretorio_destino, arquivos_selecionados):
    os.makedirs(diretorio_destino, exist_ok=True)

    for nome_arquivo in arquivos_selecionados:
        # Verifica se a extensão é exatamente .jpg
        if not nome_arquivo.endswith(".png"):
            continue

        caminho_arquivo = os.path.join(diretorio_origem, nome_arquivo)

        # Verifica se o arquivo existe
        if os.path.isfile(caminho_arquivo):
            try:
                shutil.move(caminho_arquivo, diretorio_destino)
                print(f"{nome_arquivo} movido para {diretorio_destino}.")
            except PermissionError:
                print(f"Sem permissão para mover o {nome_arquivo}.")
            except Exception as e:
                print(f"Erro ao mover {nome_arquivo}: {e}")
        else:
            print(f"Arquivo não encontrado: {nome_arquivo}")

def main():
    diretorio_origem = r"D:\Users\assis\downloads"
    diretorio_destino = r"D:\Users\assis\imagens"

    # ✅ Lista dos arquivos que você quer mover (coloque só os nomes, sem o caminho completo)
    arquivos_selecionados = [
        r"D:\Users\assis\Downloads\0df230b8-862d-4769-a6f6-9aece121c183.png"
    ]

    mover_jpgs_selecionados(diretorio_origem, diretorio_destino, arquivos_selecionados)

if __name__ == "__main__":
    main()
