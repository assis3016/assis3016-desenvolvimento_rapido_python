import os
import shutil

def criar_diretorios(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Diretório {diretorio} criado.")
            except PermissionError:
                print(f"Sem permissão para criar o diretório {diretorio}.")
            except Exception as e:
                print(f"Erro inesperado ao criar {diretorio}: {e}")

def mover_arquivo(diretorio_origem, diretorio_trabalho):
    # Percorrer todos os arquivos no diretório origem
    for pasta_atual, _, arquivos in os.walk(diretorio_origem):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, arquivo)
            extensao = arquivo.split('.')[-1].lower()

            # Verificar se a extensão está nas extensões permitidas
            if extensao in ['pdf', 'txt', 'jpg']:
                # Definir o diretório de destino com base na extensão
                diretorio_destino = os.path.join(diretorio_trabalho, extensao)

                # Criar o diretório de destino se não existir
                if not os.path.exists(diretorio_destino):
                    os.makedirs(diretorio_destino)
                    print(f"Diretório {diretorio_destino} criado.")

                try:
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(f"{arquivo} movido para {diretorio_destino}.")
                except PermissionError:
                    print(f"Sem permissão para mover o {arquivo}.")
                except Exception as e:
                    print(f"Erro inesperado ao mover {arquivo}: {e}")
            else:
                print(f"Extensão {extensao} de {arquivo} não é suportada.")

def main():
    # Caminho do diretório onde os arquivos estão localizados
    diretorio_origem = "C:/Users/assis/intro_programa_assis3016/desenvolvimento_rapido_python"

    # Caminho do diretório onde você quer que os arquivos sejam organizados
    diretorio_trabalho = "diretorio_trabalho"

    # Criar diretórios se não existirem
    diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                  os.path.join(diretorio_trabalho, 'txt'),
                  os.path.join(diretorio_trabalho, 'jpg')]

    criar_diretorios(diretorios)

    # Mover arquivos para os diretórios correspondentes
    mover_arquivo(diretorio_origem, diretorio_trabalho)

if __name__ == "__main__":
    main()
