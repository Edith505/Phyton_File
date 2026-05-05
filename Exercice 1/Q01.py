class Machine:
    def __init__(self, id, nom, adresse_ip):
        self.id = id
        self.nom = nom
        self.adresse_ip = adresse_ip
        
    def afficher(self):
        print(f"{self.id} - {self.nom} - {self.adresse_ip}")
    
    
def lire_machine(fichier):  
    machines = []
    with open(fichier,"r") as f:
        lignes = f.readlines()
        
        for ligne in lignes[1:]:
            id, ip, nom = ligne.strip().split(',')
            machine = Machine(int(id), nom, ip)
            machines.append(machine)
    return machines

def rechercher_machine(machines, ip):
    for m in machines:
        if m.adresse_ip == ip:
            return m
    return None
        
if __name__ == '__main__':
    machines = lire_machine("Exercice 1/machines.csv")
    ip_recherche = input("Entrer une adresse IP : ")
    resultat = rechercher_machine(machines, ip_recherche)
    if resultat:
        resultat.afficher()
    else:
        print("Machine introuvable")
