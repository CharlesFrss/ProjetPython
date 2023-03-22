#!/usr/bin/python3

import os
import sys
import subprocess
# Installation des dépendances nécessaires
#os.system("sudo apt-get update")
#os.system("sudo apt-get install nmap")
#os.system("sudo apt-get install python3-pip")
#subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
#pip install -r requirements.txt

import nmap
from googlesearch import search
import whois
import requests
import re
import time
import datetime
import random
from bs4 import BeautifulSoup
sc = nmap.PortScanner()

# Cette fonction permet d'effectuer un scan NMAP sur une adresse IP cible et d'enregistrer les résultats dans un fichier texte.
# Les numéros de ports ouverts sont également affichés à l'utilisateur.
def scan():
    print("Bienvenue dans l'outil de scan NMAP")
    ip = input("Ajouter l'adresse IP cible: ")
    #try et except permet la gestion d'erreur
    try:
        sc.scan(ip, '1-1024')
        print(sc.scaninfo())
        print(sc[ip]['tcp'].keys())
        scan_results = str(sc[ip])
        filename = f"nmap_{ip}.txt"
        export_result(filename, scan_results, ip)
    except Exception as e:
# En cas d'erreur, affiche un message d'erreur avec l'exception levée
        print(f"Erreur lors du scan NMAP: {e}")

# Cette fonction permet d'effectuer un scan de vulnérabilité avancé en utilisant la commande nmap sur une adresse IP cible
def vulnerabilité(ip):
    print("bienvenue sur le scan de vulnérabilité nmap avancé")
    try: 
#Les options -sV et -Pn sont utilisées pour effectuer une détection de version et éviter la détection de ping.
        result = os.popen(f'nmap -sV -Pn {ip}').read().strip()
#Les résultats du scan de vulnérabilité sont affichés à l'utilisateur.
        print(result)
        filename = f"vulnerabilite_{ip}.txt"
#Les résultats dans un fichier texte. 
        export_result(filename, result, ip)
    except Exception as e:
        print(f"Erreur lors du scan de vulnérabilité NMAP: {e}")

# Cette fonction permet d'effectuer un scan Nikto sur une adresse IP cible
def nikto(ip):
    print("Bienvenue dans l'outil de scan nikto")
    try:
        result = os.popen(f'nikto -h {ip}').read().strip()
        print(result)
        filename = f"nikto_{ip}.txt"
# Enregistre les résultats dans un fichier texte.
        export_result(filename, result, ip)
    except Exception as e:
        print(f"Erreur lors du scan Nikto: {e}")

# Cette fonction permet de créer un fichier texte. 
# Le nom de fichier est personnalisé en utilisant l'adresse IP cible
def export_result(filename, content, ip):
# Determine le chemin du dossier Bureau de l'utilisateur actuel
    chemin_machine = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# Determine le chemin complet du fichier en combinant le chemin du dossier Bureau et le nom de fichier
    chemin_fichier = os.path.join(chemin_machine, filename)
    try:
        with open(chemin_fichier, 'w') as f:
# Ouvre le fichier en mode écriture et écrit le contenu
            f.write(content)
# Confirmation de la création du fichier avec le nom ainsi que le chemin
        print(f"Le fichier {filename} a été créé avec succès dans {chemin_machine}.")
    except Exception as e:
        print(f"Erreur lors de la création du fichier: {e}")


# Cette fonction permet de créer un fichier texte. 
# Le nom de fichier est personnalisé en utilisant le nom de domaine
def export_result2(filename, content, domain_name):
    chemin_machine = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    chemin_fichier = os.path.join(chemin_machine, filename)
    try:
        with open(chemin_fichier, 'w') as f:
            f.write(content)
        print(f"Le fichier {filename} a été créé avec succès dans {chemin_machine}.")
    except Exception as e:
        print(f"Erreur lors de la création du fichier: {e}")

def export_result3(filename, content):
    chemin_machine = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    chemin_fichier = os.path.join(chemin_machine, filename)
    try:
        with open(chemin_fichier, 'w') as f:
            f.write(content)
        print(f"Le fichier {filename} a été créé avec succès dans {chemin_machine}.")
    except Exception as e:
        print(f"Erreur lors de la création du fichier: {e}")


# Cette fonction permet d'effectuer une recherche Google dorks en utilisant les informations fournies par l'utilisateur.
def DORKS():
    print("Bienvenue dans l'outil de recherche")
# Demande à l'utilisateur de fournir les informations souhaitées
    company_name = input("Nom de l'entreprise : ")
    username = input("Nom d'utilisateur : ")
    email = input("Adresse e-mail : ")
# Liste des sites utilisés pour lancer la recherche
    query = "intext:\"{0}\" OR intext:\"{1}\" site:linkedin.com OR site:glassdoor.com OR site:zoominfo.com site:facebook.com OR site:twitter.com OR site:instagram.com OR site:pinterest.com OR site:crunchbase.com OR site:hunter.io OR site:owler.com OR site:data.com OR site:hoovers.com site:*.example.com".format(company_name, username, email)
# Créer une liste vide afin de stocker les resultats de la recherche
    results = []
 # Effectue la recherche en utilisant la requête et stocke les résultats dans la liste.
    for url in search(query, num_results=10):
        results.append(url)
        print(url)
        time.sleep(10)  # Délai de 10 secondes entre chaque recherche
# Exporte les résultats dans un fichier texte en utilisant la fonction export_result3
    export_result3(f'dorks_{company_name}_{username}_{email}.txt', '\n'.join(results))

# Cette fonction utilise le module `whois` pour réaliser un WHOIS lookup sur un nom de domaine donné
def OSINT(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception as e:
        print(f"Erreur lors de la recherche WHOIS : {e}")
        return
    
# Affiche et stockez certaines informations clés de la recherche WHOIS
    print(f"Nom de domaine : {w.domain_name}")
    print(f"Registrar : {w.registrar}")
    print(f"Date d'expiration : {w.expiration_date}")
    print(f"Date de création : {w.creation_date}")
    print(f"Serveurs de noms : {w.name_servers}")
    print(f"Statut : {w.status}")
# Créer une liste vide afin de stocker les resultats de la recherche
    results = []
    results.append(f"Nom de domaine : {w.domain_name}")
    results.append(f"Registrar : {w.registrar}")
    results.append(f"Date d'expiration : {w.expiration_date}")
    results.append(f"Date de création : {w.creation_date}")
    results.append(f"Serveurs de noms : {w.name_servers}")
    results.append(f"Statut : {w.status}")

    filename = f"osint_{domain_name}.txt"
# Exporte les résultats dans un fichier texte en utilisant la fonction export_result2
    export_result2(filename, '\n'.join(results), domain_name)


# Cette fonction utilise le module `emailharvester` pour réaliser un scan d'adresse e-mail sur un nom de domaine donné
def emailharvester(domain_name):
    print("Bienvenue sur le scan d'email : ")
    try:
        email = os.popen('emailharvester -d ' + domain_name).read().strip()
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")
        return
    # Chercher toutes les adresses e-mail avec une expression régulière
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)

    # Afficher les adresses e-mail trouvées
    for email in emails:
        print(email)

    # Exporter les adresses email dans un fichier
    filename = f"email_{domain_name}.txt"
    try:
        with open(filename, "w") as file:
            file.write("\n".join(emails))
    except Exception as e:
        print(f"Erreur lors de l'exportation : {e}")
        return
    print(f"{len(emails)} adresses email trouvées. Exporté dans le fichier {filename}.")
    


def veille_sécurité():
    # Source de renseignements ouverts
    url = "https://nvd.nist.gov/general/nvd-dashboard"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
# Requête HTTP avec l'URL et les en-têtes définis ci-dessus
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Gestion des erreurs HTTP
    except requests.exceptions.HTTPError as errh:
        print(f"Une erreur HTTP s'est produite: {errh}")
        return
    except requests.exceptions.RequestException as err:
        print(f"Une erreur s'est produite: {err}")
        return
# Analyse du contenu HTML de la page web avec la bibliothèque BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
# Recherche de la première div avec la classe "col-md-12 col-sm-12"
    div = soup.find("div", {"class": "col-md-12 col-sm-12"})

    if div is None:
        print("La div n'a pas été trouvée.")
        return
# Recherche de tous les éléments "li" à l'intérieur de la div trouvée ci-dessus
    lis = div.find_all("li")

    if len(lis) == 0:
        print("Aucun élément 'li' trouvé à l'intérieur de la div.")
        return
# Concaténation des textes de tous les éléments "li" en une seule chaîne de caractères
    informations = ""
    for li in lis:
        informations += li.text + "\n"
#import de la date et heure pour le nom du fichier
    date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"veille_securite_{date_now}.txt"

    try:
# Exportation des informations dans le fichier
        with open(filename, "w") as f:
            f.write(informations)
        print(f"Les informations de la veille sécurité ont été exportées dans le fichier {filename} dans le dossier ProjetPython")
    except IOError as err:
        print(f"Une erreur s'est produite lors de l'exportation des informations: {err}")
        return


def dorks_domaine():
    
    print(f"Recherche d'URL liées au domaine {domain_name} : ")
# Une liste de chaînes de caractères est créée, chacune étant une requête de recherche à envoyer à Google pour trouver des URL liées au domaine donné.  
    dorks = [
        "site:{}".format(domain_name),
        "intitle:index.of {}".format(domain_name),
        "inurl:{}".format(domain_name),
        "filetype:pdf site:{}".format(domain_name),
        "filetype:xls site:{}".format(domain_name),
        "filetype:doc site:{}".format(domain_name),
        "filetype:ppt site:{}".format(domain_name),
        "filetype:csv site:{}".format(domain_name),
        "filetype:txt site:{}".format(domain_name),
        "filetype:conf site:{}".format(domain_name),
    ]
# Une liste d'agents utilisateurs est créée. Ces chaînes de caractères sont utilisées pour simuler différents navigateurs Web lors de l'envoi de requêtes à Google.
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"
    ]
    
    # Créer un nom de fichier unique basé sur la date et l'heure actuelles
    # cela évite d'écraser les recherches précedentes
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"urls-{domain_name}-{timestamp}.txt"

# Chaque requête dans la liste dorks est envoyée à Google avec un agent utilisateur choisi au hasard. 
# Le contenu de la réponse est analysé pour extraire les URL, qui sont ensuite écrites dans le fichier

    with open(filename, "w") as f:
        for dork in dorks:
            url = "https://www.google.com/search?q={}".format(dork)
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(url, headers=headers)

            results = re.findall('href="([^"]+)"', response.text)

            for result in results:
                if "google.com" not in result:
                    print(result)
                    f.write(result + "\n")

            time.sleep(random.uniform(4, 10))
            
    print(f"Les résultats ont été enregistrés dans le fichier {filename}.")

# La boucle while maintient le menu en cours d'exécution jusqu'à ce que l'utilisateur choisisse de quitter.
while True:
# Affiche les options du menu principal.
    print("\nMAIN MENU")
    print("1. Test d'intrusion")
    print("2. OSINT")
    print("3. Quitter le programme.")
# Invite l'utilisateur à saisir son choix.
    choice1 = int(input("Enter the Choice:"))
# S'exécute si l'utilisateur choisit l'option 1 .
    if choice1 == 1:
# Affiche les options du menu de test d'intrusion .
        print("\nCHOIX DU SCAN")
        print("1. SCAN RAPIDE")
        print("2. HARD SCAN")
        print("3. RETOUR")
# Invite l'utilisateur à saisir son choix.
        choice2 = int(input("Faire un choix: "))
# S'exécute si l'utilisateur choisit l'option 1 dans le menu Test d'intrusion .
        if choice2 == 1:
# Execute la fonction scan
            print("Vous avez choisi le SCAN RAPIDE")
            scan()

# S'exécute si l'utilisateur choisit l'option 2 dans le menu Test d'intrusion.       
        elif choice2 == 2:
# Execute la fonction vulnerabilité et nikto
            print("Vous avez choisi le HARD SCAN")
# Invite l'utilisateur à écrire l'adresse ip
            ip = input("Ajouter l'adresse IP cible : ")
            vulnerabilité(ip)
            nikto(ip)
# Permet de faire un retour au menu principale
        elif choice2 == 3:
            continue
# Le script se termine si le choix est incorrect
        else:
            print("Choix incorrect, merci de faire un choix entre 1 et 5.")
            break
# S'exécute si l'utilisateur choisit l'option 2 .
    elif choice1 == 2:
# Affiche les options du menu 2ème menu.
        print("\nCHOIX DE LA METHODE")
        print("1. GOOGLE DORKS")
        print("2. Domaine et email")
        print("3. Veille Informatique")
        print("4. Retour")
# Invite l'utilisateur à saisir son choix.
        choice3 = int(input("Faire un choix: "))

# S'exécute si l'utilisateur choisit l'option 1 dans le menu OSINT.
        if choice3 == 1:
            print("Vous avez choisi le GOOGLE DORKS")
            domain_name = input("Ajouter le nom de domaine cible : ")
            DORKS()
            dorks_domaine()
 # S'exécute si l'utilisateur choisit l'option 2 dans le menu OSINT.       
        elif choice3 == 2:
            print("Vous avez choisi la recherche de Domaine et d'email")
            domain_name = input("Entrez le nom de domaine à rechercher: ")

            OSINT(domain_name)
            emailharvester(domain_name)

# S'exécute si l'utilisateur choisit l'option 3 dans le menu OSINT.
        elif choice3 == 3:
            print("vous avec choisi la Veille Informatique")
            veille_sécurité()

# Permet de faire un retour au menu principale
        elif choice3 == 4:
            continue

        else:
            print("Choix incorrect, merci de faire un choix entre 1 et 4.")
            break
        
# Permet de quitter le programme       
    elif choice1 == 3:
        exit()
    
    else: 
        print("Choix incorrect, merci de faire un choix entre 1 et 3.")
        continue
