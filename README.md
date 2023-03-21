# Outil de d'analyse de vulnérabilité et de recherche d'information

Ce programme est un ensemble d'outils de sécurité destiné aux tests de pénétration et à la sécurité des réseaux. Il utilise les bibliothèques Python pour lancer des scans de ports, de vulnérabilités et d'emails, et pour effectuer des recherches d'informations sur les noms de domaine.

Il permet de tester la sécurité des systèmes informatiques comme scanner les ports ouverts, détecter les vulnérabilités et d'effectuer des scans Nikto sur une adresse IP cible. Il a également la capacité de collecter des informations via de l’OSINT sur des noms de domaines, des entreprises ainsi que des vulnérabilités nouvellement plubliées de manière efficace. Il utilise plusieurs dépendances telles que nmap, googlesearch-python, python-whois et beautifulsoup4.

## Prérequis

Pour une utilisation optimale il est recommandé d’utiliser ce script sur une distribution Parrot. L’ensemble du développement a été réalisé sur cette dernière ce qui assurera son bon fonctionnement. Une partie des dépendances mentionné ci-dessous sont déjà installer sur la Parrot.
Pour autant le script comporte les commandes nécessaires et le lancement de ce dernier installe les dépendances nécessaires automatiquement. Cependant elles sont tout de même mentionnée à titre informatif et en cas de bug du script.

- Python 3
 ```bash
sudo apt-get update
 ```
 ```bash
sudo apt-get install python3
 ```
- Python3 pip
 ```bash
 sudo apt-get python3-pip
 ```
- python-nmap : un scanner de port open source. 
 ```bash
 pip3 install python-nmap
 ```
- googlesearch-python : une bibliothèque pour effectuer des recherches sur Google.
```bash
pip3 install googlesearch-python
```
- python-whois : une bibliothèque pour obtenir des informations sur les noms de domaine.
```bash
pip3 install python-whois
```
- beautifulsoup4 : une bibliothèque pour extraire des informations à partir de pages Web.
```bash
pip3 install beautifulsoup4
```
- emailharvester : une bibliothèque pour récupérer les adresses e-mail à partir d'un nom de domaine.


## Installation

1. Cloner ce repository sur votre machine locale
2. Installer les prérequis ci-dessus
3. Exécuter le script à l'aide de Python 3 en utilisant la commande `python3 nom du script.py`

## Fonctionnalités

Le programme se compose de plusieurs fonctions :

- Scan des ports ouverts pour une adresse IP donnée avec nmap
- Scan de vulnérabilités avancé avec nmap
- Scan de vulnérabilités Web avec nikto
- Utilisation de Dorks pour rechercher des informations sur une entreprise, un nom d'utilisateur ou une adresse e-mail
- Investigation OSINT sur des noms de domaines
- Scan d'email harvesting
- Recherche de CVEC up-to-date via du scrapping web sur le site de NIST

## Utilisation

Pour utiliser le programme, exécutez simplement le fichier nomduscript.py avec Python 3 :

Le programme propose les options suivantes :

1. Scan Nmap

Pour lancer un scan de ports et de vulnérabilités avec nmap, sélectionnez l'option correspondante dans le menu principal.
Faire le choix `1. Test d'intrusion` puis `1. SCAN RAPIDE`
Vous serez invité à entrer l'adresse IP de la cible. Le programme effectuera ensuite un scan des ports 1 à 1024 et affichera les résultats. Le scan peut être personnalisé en modifiant les options passées à `sc.scan()`. Les résultats du scan sont exportés dans un fichier texte grâce à la définition `export_result`.

2. Scan de vulnérabilité Nmap avancé + Nikto

Cette option permet de lancer un scan de vulnérabilité Nmap suivi de Nikto sur une adresse IP donnée.
Sélectionnez l'option correspondante dans le menu principal : 
`1. Test d'intrusion` puis `2. HARD SCAN`.
Voici le fonctionnement plus précisément :
- Le programme effectue un scan de vulnérabilité avec l'option `-sV -Pn` de nmap
- Le programme effectue ensuite un scan de vulnérabilité avec Nikto et l'option `nikto -h` qui peut du coup être modifié selon vos besoins
Les résultats des scans sont exportés indépendamment dans un fichier texte, le chemin est affiché à la fin de chaque processus grâce à la définition `export_result`.

3. Recherche de Dorks

Cette option permet d'effectuer une recherche de dorks Google en utilisant un nom d'entreprise, un nom d'utilisateur ou une adresse e-mail. Pour lancer une recherche de DORKS sur des entreprises et des utilisateurs, sélectionnez l'option correspondante dans le menu principal:
`2. OSINT` puis `1. GOOGLE DORKS`

Vous serez invité à entrer le nom de l'entreprise, le nom d'utilisateur et l'adresse e-mail que vous souhaitez rechercher.
Notez qu'il est possible de ne renseigner que certaines donné par exemple juste une adresse mail ou une entreprise.
Le programme effectuera ensuite une recherche Google à l'aide de la requête `intext:"{company_name}" OR intext:"{username}" OR intext:"{email}" site:linkedin.com OR site:glassdoor.com OR site:zoominfo.com site:facebook.com OR site:twitter.com OR site:instagram.com OR site:pinterest.com OR site:crunchbase.com OR site:hunter.io OR site:owler.com OR site:data.com OR site:hoovers.com site:*.example.com" OR site`

Ce choix execute également un recherche qui prend en entrée un nom de domaine et effectue une recherche de différents types de fichiers liés à ce domaine (PDF, XLS, DOC, PPT, CSV) en utilisant différents opérateurs Google (site, intitle, inurl, filetype). Les résultats sont affichés à l'écran.

Ces fonction peuvent être modifiée en fonction des besoins souhaité notamment en ajoutant des en-tête permettant d'utliser d'autre navigateur web, en modifiant les sites souhaités ainsi que le time sleep qui peux augmenter le nombre de résultats.
Il est recommandé d'utiliser un proxy ou un VPN dans le but d'éviter tout blocage/banissement des navigateurs webs.

Les résultats des scans sont exportés indépendamment dans un fichier texte, le chemin est affiché à la fin de chaque processus grâce à la définition `export_result3` et un ajout à la suite de la fonction `dorks_domaine`.


4. OSINT

Cette option permet d'obtenir des informations sur un nom de domaine en utilisant la bibliothèque Python-whois.
Pour lancer une recherche d'OSINT sur des nom de domaine, sélectionnez l'option correspondante dans le menu principal:
`2. OSINT` puis `2. Domaine et email`
Cette fonction prend en entrée un nom de domaine et effectue une recherche WHOIS pour obtenir des informations sur ce domaine, telles que le nom de domaine, le registrar, la date d'expiration, la date de création, les serveurs de noms et le statut. Elle exporte également les résultats dans un fichier texte grâce à la définition `export_result2`.

Cette option permet de récupérer les adresses e-mail associées à un nom de domaine donné. Elle prend en entrée un nom de domaine et recherche toutes les adresses e-mail associées à ce domaine en utilisant l'outil EmailHarvester. Elle exporte ensuite les adresses e-mail trouvées dans un fichier texte.


5. Veille sécurité (Scrapping)

Cette option effectue une veille de la sécurité en extrayant les CVEC les plus récentes présentes sur le site Web de NIST (National Institute of Standards and Technology) et les exporte dans un fichier texte.
Elle utilise la bibliothèque Beautifulsoup4 afin de pouvoir parser le code HTML souhaité.
Il est donc possible de modifier le code afin de pouvoir parser d'autres sites en se référant aux différentes balises HTML présentes sur ce dernier.
Cependant certains site n'autorise pas ce genre de méthode et peuvent donc bloquer la requête.
Les résultats son exportés dans un fichier texte.


## Auteur

Ce programme a été écrit par Charles Fresse et a été créé à des fins éducatives uniquement. Il est fourni "tel quel" sans aucune garantie. Veuillez utiliser ce programme de manière responsable et avec la permission des propriétaires des systèmes que vous scannez. L'auteur ne sera pas tenu responsable de toute utilisation abusive ou illégale de ce programme.
De plus, certaines fonctionnalités peuvent être considérées comme intrusives ou illégales dans certaines juridictions. Il est de la responsabilité de l'utilisateur

