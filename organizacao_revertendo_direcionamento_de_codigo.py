import os
import shutil

def mover_de_volta(diretorio_origem, diretorio_destino):
    # Procurar todos os arquivos em subpastas de 'diretorio_origem' e movê-los de volta para 'diretorio_destino'
    for pasta_atual, _, arquivos in os.walk(diretorio_origem):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, arquivo)

            # Verifica se o arquivo não está no diretório de destino
            if pasta_atual == diretorio_destino:
                continue
            
            try:
                shutil.move(caminho_arquivo, diretorio_destino)
                print(f"{arquivo} movido de volta para {diretorio_destino}.")
            except PermissionError:
                print(f"Sem permissão para mover o {arquivo} de volta.")
            except Exception as e:
                print(f"Erro ao mover {arquivo} de volta: {e}")

def main():
    # Caminho para o diretório de origem onde os arquivos estão (diretório 'jpg'.)
    diretorio_origem = r"D:\Users\assis\imagens"
    
    # Caminho para o diretório principal onde os arquivos devem ser movidos de volta
    diretorio_destino = r"D:\Users\assis"
    
    # Mover os arquivos de volta para o diretório principal
    mover_de_volta(diretorio_origem, diretorio_destino)

if __name__ == "__main__":
    main()
