# Projet-Big-Data
Groupe : Christ / Fatima / Christopher / Dorian

Langage requis : Python 3.5 ou une version stable recommandée

Modules Python à installer : Sys / Pandas / datetime / decimal / Matplotlib.pyplot / Sample / csv / happybase
- sys
- pandas
- datetime
- decimal
- matplotlib.pyplot
- sample
- csv
- happybase 

API utilisée: Apache Hbase Rest

Ce dossier contient des scripts Python commentés avec des docstrings expliquant leurs objectifs et leur utilisation.
L'utilisateur a le choix de lancer les scripts directement depuis un IDE compatible Python ou depuis Hadoop (nécessaire pour HBase - Lot3).

-Attention ! Les répertoires des dossiers doivent être commentés et décommentés selon l'environnement (IDE/Hadoop).

Pour Hadoop:
- Exécution de l'environnement Hadoop et modification ou configuration des dossiers appropriés.
- Lancement d'un job MapReduce avec la commande (exemple pour le lot 1):
    - hadoop jar hadoop-streaming-2.7.2.jar -file mapper_lot1.py -mapper "python3 mapper_lot1.py" -file reducer_lot1.py -reducer "python3 reducer_lot1.py" -input input/dataw_fro03.csv -output output/output_lot1_exo1
- Vérification des résultats dans le répertoire de sortie approprié.

Veuillez noter que le processus d'analyse et d'exécution des scripts doit être effectué avec soin pour garantir des résultats précis et fiables.


 LOT 1
•
Contexte :
•
Une Fromagerie (le client) a un datawarehouse depuis 2004 qui est représenté par le fichier csv fournit dans ce document.
•
Créer des jobs pour limiter le flux d’information (Mapper-Reducer) pour obtenir uniquement les informations voulues pour répondre au besoin du client décrit ci-dessous :
•
Le client désire les statistiques suivantes :

1) Filtrer les données selon les critères suivants :
Entre 2006 et 2010,
Avec uniquement les départements 53, 61 et 28

2) A partir du point 1 : Ressortir dans un tableau des 100 meilleures commandes avec la ville, la somme des quantités des articles et la valeur de « timbrecde » (la notion de meilleures commandes : la somme des quantités la plus grande ainsi que le plus grand nombre de « timbrecde » )

3) Exporter le résultat dans un fichier Excel.


LOT 2
•
Contexte :
•
Une Fromagerie (le client) a un datawarehouse depuis 2004 qui est représenté par le fichier csv fournit dans ce document.
•
Le client désire les statistiques suivantes :

1) Filtrer les données selon les critères suivants :
Entre 2011 et 2016,
Avec uniquement les départements 22, 49 et 53

2) A partir du point 1 : Ressortir de façon aléatoire de 5% des 100 meilleures commandes avec la ville, la somme des quantités des articles sans « timbrecli » (le timbrecli non renseigné ou à 0) avec la moyenne des quantités de chaque commande)
Avoir un PDF avec un graphe (PIE) (par Ville)

3) Exporter le résultat dans un fichier Excel.
