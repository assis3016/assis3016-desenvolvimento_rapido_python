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
    # Caminho para o diretório de origem onde os arquivos estão (diretório 'pdf', 'txt', etc.)
    diretorio_origem = "C:/Users/assis/intro_programa_assis3016/desenvolvimento_rapido_python/.vscode/diretorio_trabalho"
    
    # Caminho para o diretório principal onde os arquivos devem ser movidos de volta
    diretorio_destino = "C:/Users/assis/intro_programa_assis3016/desenvolvimento_rapido_python"
    
    # Mover os arquivos de volta para o diretório principal
    mover_de_volta(diretorio_origem, diretorio_destino)

if __name__ == "__main__":
    main()
