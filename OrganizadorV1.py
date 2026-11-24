# Atividade aula 13 Terminar o organizador: sys.argv, Path(__file__).parent, logging em arquivo e --simular

from pathlib import Path

organizador_v1 = '''
import shutil
from pathlib import Path

PASTA = Path("Downloads_teste")

GRUPOS = {
    "PDFs":      [".pdf"],
    "Imagens":   [".jpg", ".jpeg", ".png"],
    "Planilhas": [".csv", ".xlsx"],
}

def grupo_de(sufixo):
    for nome, extensoes in GRUPOS.items():
        if sufixo.lower() in extensoes:
            return nome
    return "Outros"

movidos = 0
for item in PASTA.iterdir():
    if item.is_dir():
        continue
    destino = PASTA / grupo_de(item.suffix)
    destino.mkdir(exist_ok=True)
    shutil.move(item, destino / item.name)
    movidos += 1

print(f"{movidos} arquivos movidos")
'''

Path("organizador_v1.py").write_text(organizador_v1, encoding="utf-8")
print("organizador_v1.py gravado")