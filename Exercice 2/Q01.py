from pathlib import Path

class Machine:
    def __init__(self, id, nom, adress_ip):
        self.id = id
        self.nom = nom
        self.adress_ip = adress_ip
        
    def __str__(self):
        return f"{self.id} - {self.nom} - {self.adress_ip}"
        
        
def lire_fichier(fichier):
    machines = []
    chemin = Path(fichier)
    
    if not chemin.exists():
        raise FileNotFoundError("fichier n'existe pas")
    
    with open(fichier, 'r') as f:
        lignes = f.readlines()
        
    for ligne in lignes[1:]:
        id, nom, ip = ligne.strip().split(',')
        machines.append(Machine(int(id), nom, ip))
    
    return machines

def chercher_machine(machines, ip):
    for machine in machines:
        if machine.adress_ip == ip:
            return machine
    return None 