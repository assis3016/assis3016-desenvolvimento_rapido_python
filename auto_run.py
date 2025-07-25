import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MeuHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("imagem_binaria.py"):
            print("Arquivo modificado, rodando...")
            subprocess.run(["python", "imagem_binaria.py"])

caminho = "."
observer = Observer()
observer.schedule(MeuHandler(), path=caminho, recursive=False)
observer.start()

print("Observando alterações... Pressione CTRL+C para sair.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
