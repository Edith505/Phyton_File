import time

def suivre_fichier(fichier):
    with open(fichier, 'r') as f:
        f.seek(0, 2)
        
        while True:
            ligne = f.readline()
            
            if not ligne:
                time.sleep(1)
            
            print(ligne.strip())

suivre_fichier("Exercice 2/file.txt")