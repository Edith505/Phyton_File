import subprocess
import platform

def obtenir_ip():
    systeme = platform.system()
    if systeme == "Windows":
        cmd = "ipconfig"
    else:
        cmd = "ifconfig"
        
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    lignes = result.stdout.split("\n")
    
    for ligne in lignes:
        if "IPv4" in ligne or "inet " in ligne:
            print("IP trouvée :", ligne.strip())
            break
        
obtenir_ip()