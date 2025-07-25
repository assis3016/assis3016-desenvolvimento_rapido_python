import os
import shutil

# Mapeamento das extensões para os nomes das pastas de destino
EXTENSOES_PASTAS = {
    ".js": "java",
    ".md": "markdown",
    ".png": "png",
    ".gif": "gif",
    ".download": "download",
    ".dat": "dat",
    ".html": "html",
    ".svg": "svg",
    ".php": "php",
    ".py": "python",
    ".pyi": "python",
}

def encontrar_pasta_destino(nome_pasta, pasta_base):
    """Procura a pasta com o nome correspondente em todas as subpastas"""
    for raiz, pastas, _ in os.walk(pasta_base):
        if nome_pasta in pastas:
            return os.path.join(raiz, nome_pasta)
    return None

def mover_arquivos_de_pasta_origem(pasta_origem, pasta_base_destino):
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(nome_arquivo)
            extensao = extensao.lower()

            if extensao in EXTENSOES_PASTAS:
                nome_pasta_destino = EXTENSOES_PASTAS[extensao]
                caminho_pasta_destino = encontrar_pasta_destino(nome_pasta_destino, pasta_base_destino)

                if not caminho_pasta_destino:
                    print(f"⚠️ Pasta '{nome_pasta_destino}' não encontrada em nenhuma subpasta. Pulei {nome_arquivo}.")
                    continue

                try:
                    shutil.move(caminho_arquivo, os.path.join(caminho_pasta_destino, nome_arquivo))
                    print(f"✅ Movido: {nome_arquivo} → {caminho_pasta_destino}")
                except Exception as e:
                    print(f"❌ Erro ao mover {nome_arquivo}: {e}")

def main():
    pasta_origem = r"D:\Users\assis\perdidos"         # Onde estão os arquivos a mover
    pasta_base_destino = r"D:\Users\assis"            # Raiz onde serão procuradas as pastas 'python', 'php', etc.

    mover_arquivos_de_pasta_origem(pasta_origem, pasta_base_destino)

if __name__ == "__main__":
    main()
