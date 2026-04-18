# Scanner de Ports TCP Multi-threadé

Un scanner de ports réseau en ligne de commande, rapide et asynchrone, développé en Python. Cet outil permet d'identifier les ports ouverts sur une machine cible (adresse IP ou nom de domaine) en utilisant le multi-threading pour des performances optimales.

## Fonctionnalités

* **Ultra-rapide :** Utilise `concurrent.futures` avec un pool de 100 threads pour scanner de nombreux ports simultanément.
* **Flexible :** Configuration personnalisée des ports à scanner via des arguments CLI (plage de ports, liste spécifique ou port unique).
* **Gestion des délais (Timeout) :** Paramétrage du temps d'attente maximum pour éviter de bloquer sur les ports filtrés par des pare-feu.
* **Exportation des résultats :** Possibilité de sauvegarder le rapport du scan dans un fichier texte.
* **Léger :** Construit uniquement avec les bibliothèques standards de Python (aucune dépendance externe n'est requise).

## Prérequis

* Python 3.x installé sur votre machine.

## Installation

Clonez ce dépôt sur votre machine locale :

```bash
git clone [https://github.com/Aimenkhimoum/python-port-scanner.git](https://github.com/Aimenkhimoum/python-port-scanner.git)
cd python-port-scanner
```
## Utilisation

Le script s'exécute directement depuis votre terminal. 

**Syntaxe de base :**
```bash
python3 scanner.py <cible> [options]
```

### Exemples de commandes :

**1. Scan par défaut (ports 1 à 1024) :**
```bash
python3 scanner.py 192.168.1.1
```

**2. Scanner une plage de ports spécifique avec un timeout personnalisé (ex: 0.5s) :**
```bash
python3 scanner.py google.com -p 80-500 -t 0.5
```

**3. Scanner une liste de ports précis :**
```bash
python3 scanner.py 10.0.0.5 -p 21,22,80,443,8080
```

**4. Sauvegarder les résultats dans un fichier :**
```bash
python3 scanner.py 192.168.1.1 -p 1-10000 -o rapport_scan.txt
```

## ⚠️ Avertissement
Cet outil a été développé à des fins éducatives et de diagnostic personnel. Ne l'utilisez que sur des réseaux et des machines pour lesquels vous avez une autorisation explicite.
