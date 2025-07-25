import os
import shutil

def mover_jpgs(diretorio_origem, diretorio_destino):
    # Garante que o diretório de destino exista
    os.makedirs(diretorio_destino, exist_ok=True)

    # Lista apenas arquivos da primeira camada (sem subpastas)
    for nome_arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, nome_arquivo)

        # Verifica se é arquivo e termina com .jpg (minúsculo)
        if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".jpg"):
            try:
                shutil.move(caminho_arquivo, diretorio_destino)
                print(f"{nome_arquivo} movido para {diretorio_destino}.")
            except PermissionError:
                print(f"Sem permissão para mover o {nome_arquivo}.")
            except Exception as e:
                print(f"Erro ao mover {nome_arquivo}: {e}")

def main():
    diretorio_origem = r"D:\Users\assis\entrada"
    diretorio_destino = r"D:\Users\assis\imagens"

    mover_jpgs(diretorio_origem, diretorio_destino)

if __name__ == "__main__":
    main()
