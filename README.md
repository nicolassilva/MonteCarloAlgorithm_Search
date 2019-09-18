## Sujet: Repliement d'un modèle simplifié de protéine par un algorithme de Monte-Carlo et échange de répliques

Nicolas Silva (silva.nicolas.j@gmail.com)<br/>
Université Paris Diderot - Septembre 2019 - Projet court

__Objectif__

Le but de ce projet est d'implémenter une algorithme de Monte Carlo afin d'effectuer des repliements de chaîne protéiques.
Ce travail est basé sur l'article suivant :
*Thachuk C, Shmygelska A, Hoos HH. A replica exchange Monte Carlo algorithm for protein folding in the HP model. BMC Bioinformatics. 2007 Sep 17;8:342. PubMed PMID: 17875212; PubMed Central PMCID: PMC2071922.*



Exécution sous l'environnement python3

#### Répertoires et Localisation des fichiers
*********************************************

Le répertoire contient :
	* un dossier *data* contenant le fichier avec une séquence hydro/polaire d'acides aminés.
	* un dossier *doc* contenant le rapport du projet.
	* un dossier *results* contenant les résultats de repliements protéiques après l'algorithme de Monte Carlo.
	* un dossier *src* contenant le script utilisé
	* un fichier *.yml* permettant de recréer l'environnement conda utilisé

#### Programme
**************

Il n'y a qu'un seul programme à exécuter: le programme monteCarlo_Search.py
Ce programme prend 2 paramètres:
	- le premier est le fichier contenant la séquence d'intérêt
	- le second est le nombre de fois que l'algorithme de Monte Carlo doit être effectué.

''' Ex: python3 monteCarlo_Search.py 500 '''

#### Visualisation de la conformation
*************************************

La conformation finale obtenue après repliement est enregistrer dans un fichier results.txt

#### Modules python importées
*****************************

Numpy, sys
