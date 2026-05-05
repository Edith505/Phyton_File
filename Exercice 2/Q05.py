import shutil
from pathlib import Path

source = Path("E:\\Code\\420-4Q5-TP1-2433177-2461695-v2")
destination = Path("E:\\Code\\All Projet\\copie")

if destination.exists():
    shutil.rmtree(destination)

shutil.copytree(source, destination)