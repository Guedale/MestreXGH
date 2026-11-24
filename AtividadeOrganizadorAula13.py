
import shutil
import sys
import logging
from pathlib import Path


# LOCALIZAÇÃO DAS PASTAS
BASE_DIR = Path(__file__).parent
PASTA = BASE_DIR / "Downloads_teste"
ARQUIVO_LOG = BASE_DIR / "organizador.log"


# TIPOS DE ARQUIVOS
GRUPOS = {
    "PDFs": [".pdf"],
    "Imagens": [".jpg", ".jpeg", ".png"],
    "Planilhas": [".csv", ".xlsx"],
}


# IDENTIFICAR O GRUPO DO ARQUIVO
def grupo_de(sufixo):
    for nome, extensoes in GRUPOS.items():
        if sufixo.lower() in extensoes:
            return nome

    return "Outros"


# CONFIGURAR O LOGGING
def configurar_logging():
    logging.basicConfig(
        filename=ARQUIVO_LOG,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )


# ORGANIZAR OS ARQUIVOS
def organizar(simular=False):
    movidos = 0

    if not PASTA.exists():
        print("A pasta Downloads_teste não foi encontrada.")
        logging.error("Pasta não encontrada: %s", PASTA)
        return

    for item in PASTA.iterdir():

        if item.is_dir():
            continue

        grupo = grupo_de(item.suffix)
        destino = PASTA / grupo
        caminho_destino = destino / item.name

        if caminho_destino.exists():
            logging.warning("Arquivo já existe: %s", caminho_destino)
            continue

        if simular:
            print(f"[SIMULAÇÃO] {item.name} -> {grupo}")
            logging.info("[SIMULAÇÃO] %s -> %s", item, caminho_destino)

        else:
            destino.mkdir(exist_ok=True)
            shutil.move(str(item), str(caminho_destino))

            print(f"Movido: {item.name} -> {grupo}")
            logging.info("Movido: %s -> %s", item, caminho_destino)

        movidos += 1

    if simular:
        print(f"Simulação concluída: {movidos} arquivos seriam movidos.")
    else:
        print(f"Organização concluída: {movidos} arquivos movidos.")


# INICIAR O PROGRAMA
def main():
    configurar_logging()

    simular = "--simular" in sys.argv

    organizar(simular)


if __name__ == "__main__":
    main()