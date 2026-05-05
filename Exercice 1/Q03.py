from pathlib import Path

path = Path(r"E:\DEC CEGEP LIMOILOU\SESSION 4\109-330-LI Conditionnement Physique")

for chemin in path.glob("*.pdf"):
    print("Absolu : ", chemin.resolve())
    print("Relatif :", chemin.relative_to(path))
    print("-" * 40)

for root, dirs, files in path.walk():
   for f in files:
        fpath = root / f
        if fpath.suffix.lower() == ".pdf":
            print("Absolu :", fpath.resolve())
            print("Relatif :", fpath.relative_to(path))
            print("=" * 40)


    
    
    