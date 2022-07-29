# Projet 11 - Améliorez une application Web Python par des tests et du débogage - OpenClassrooms

Cet application web permet de rationaliser la gestion des compétitions entre les clubs (hébergement, inscriptions, frais et administration).

## Mise en place du projet: 

#### I) Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.

###### - Récupération du projet

    $ git clone https://github.com/Appryll/Projet-11-Am-liorez-une-application-Web-Python-par-des-tests-et-du-d-bogage.git

    Se déplacer dans le repertoire du projet :

    $ cd Projet-11-Am-liorez-une-application-Web-Python-par-des-tests-et-du-d-bogage-master

###### -Créer et activer l'environnement virtuel 
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement
    > set FLASK_APP=run
    > flask run

    Le site sera accéssible à l'adresse local : 127.0.0.1:5000 sur le port 5000 par défaut.

###### - Quitter le serveur de developpement
    CTRL+C

###### - Quitter l'envirement virtuel
    deactivate

-----
#### II) MacOS, Linux :
Dans le terminal, naviguer vers le dossier souhaité.

###### - Récupération du projet
     $ git clone https://github.com/Appryll/Projet-11-Am-liorez-une-application-Web-Python-par-des-tests-et-du-d-bogage.git

    Se déplacer dans le repertoire du projet :
    $ cd Projet-11-Am-liorez-une-application-Web-Python-par-des-tests-et-du-d-bogage-master

###### -Créer et activer l'environnement virtuel
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    $ export FLASK_APP=run
    $ flask run

    Le site sera accéssible à l'adresse local : 127.0.0.1:5000 sur le port 5000 par défaut.

###### - Quitter le serveur de developpement
    CTRL+C

###### - Quitter l'envirement virtuel
    deactivate

------------------------------------------------------------------------------------------------------------------------
## Améliorations concernant la phase 3: 

- Bouton "return" dans 'booking'
- Bouton "return" dans 'list of points available for each club'
- 