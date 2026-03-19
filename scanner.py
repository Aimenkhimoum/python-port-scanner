#!/usr/bin/env python3

import sys
import socket
from datetime import datetime
import concurrent.futures
import argparse

# configuration des arguments en ligne de commande
parser = argparse.ArgumentParser(description="Scanner de ports réseau rapide en Python")
parser.add_argument("target", help="L'adresse IP ou le nom de domaine à scanner (ex: 192.168.1.1 ou google.com)")
parser.add_argument("-p", "--ports", default="1-1024", help="Plage de ports (ex: 1-1000) ou liste (ex: 22,80,443)")
parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Délai d'attente max par port en secondes (défaut: 1.0)")
parser.add_argument("-o", "--output", help="Nom du fichier pour sauvegarder les résultats (ex: resultats.txt)")
args = parser.parse_args()

#  résolution de la cible
try:
    target_ip = socket.gethostbyname(args.target)
except socket.gaierror:
    print(f"Erreur : Impossible de résoudre le nom d'hôte {args.target}")
    sys.exit()

#  traitement de l'argument des ports
ports_to_scan = []
if "-" in args.ports:
    start, end = map(int, args.ports.split("-"))
    ports_to_scan = range(start, end + 1)
elif "," in args.ports:
    ports_to_scan = [int(p) for p in args.ports.split(",")]
else:
    ports_to_scan = [int(args.ports)]

open_ports = []

print("-" * 60)
print(f"Scan de la cible : {target_ip} ({args.target})")
print(f"Heure de début   : {datetime.now()}")
print("-" * 60)

# fonction de scan avec Timeout
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(args.timeout) # évite au script de bloquer sur un port silencieux
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} est ouvert")
            open_ports.append(port)
        s.close()
    except (socket.gaierror, socket.error):
        pass

#  on fait l'Exécution Multi-threadée
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, ports_to_scan)
except KeyboardInterrupt:
    print("\nArrêt du programme par l'utilisateur.")
    sys.exit()

# on fait l'xportation des résultats
if args.output:
    try:
        with open(args.output, "w") as f:
            f.write(f"Résultats du scan pour {args.target} ({target_ip})\n")
            f.write(f"Date: {datetime.now()}\n")
            f.write("-" * 40 + "\n")
            if open_ports:
                for port in sorted(open_ports):
                    f.write(f"Port {port} : Ouvert\n")
            else:
                f.write("Aucun port ouvert trouvé.\n")
        print(f"\n[i] Les résultats ont été sauvegardés avec succès dans '{args.output}'")
    except Exception as e:
        print(f"\n[!] Erreur lors de la sauvegarde du fichier : {e}")