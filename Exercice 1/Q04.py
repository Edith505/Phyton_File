from pathlib import Path
path = Path(r"E:\DEC CEGEP LIMOILOU\SESSION 4\109-330-LI Conditionnement Physique")

nombre_de_fichiers = 0
taille_totale = 0
plus_gros_fichier = ("", 0)

for fichier in path.rglob("*"):
    if fichier.is_file():
        nombre_de_fichiers += 1
        taille_fichier = fichier.stat().st_size
        taille_totale += taille_fichier
        
        if taille_fichier > plus_gros_fichier[1]:
            plus_gros_fichier =(fichier.name, taille_fichier)
    
print("Fichiers :", nombre_de_fichiers)
print(f"Taille totale (KO) : {taille_totale / 1024:.2f}")
print("Plus gros fichier :", plus_gros_fichier[0], "-", plus_gros_fichier[1], "octets")