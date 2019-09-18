## Sujet: Repliement d'un modèle simplifié de protéine par un algorithme de Monte-Carlo et échange de répliques

Nicolas Silva (silva.nicolas.j@gmail.com)<br/>
Université Paris Diderot - Septembre 2019 - Projet court

__Objectif__

Le but de ce projet est d'implémenter une algorithme de Monte Carlo afin d'effectuer des repliements de chaîne protéiques.<br/><br/>
Ce travail est basé sur l'article suivant :
*Thachuk C, Shmygelska A, Hoos HH. A replica exchange Monte Carlo algorithm for protein folding in the HP model. BMC Bioinformatics. 2007 Sep 17;8:342. PubMed PMID: 17875212; PubMed Central PMCID: PMC2071922.*



Exécution sous l'environnement python3

#### Répertoires et Localisation des fichiers
*********************************************

Le répertoire contient :<br/>
	- un dossier *data* contenant le fichier avec une séquence hydro/polaire d'acides aminés.<br/>
	- un dossier *doc* contenant le rapport du projet.<br/>
	- un dossier *results* contenant les résultats de repliements protéiques après l'algorithme de Monte Carlo.<br/>
	- un dossier *src* contenant le script utilisé<br/>
	- un fichier *.yml* permettant de recréer l'environnement conda utilisé<br/>

#### Programme
**************

Il n'y a qu'un seul programme à exécuter: le programme monteCarlo_Search.py<br/>
Ce programme prend 2 paramètres:<br/>
	- le premier est le fichier contenant la séquence d'intérêt.<br/>
	- le second est le nombre de fois que l'algorithme de Monte Carlo doit être effectué.<br/>

''' Ex: python3 monteCarlo_Search.py 500 '''

#### Visualisation de la conformation
*************************************

La conformation finale obtenue après repliement est enregistrer dans un fichier results.txt

#### Modules python importées
*****************************

Numpy, sys
