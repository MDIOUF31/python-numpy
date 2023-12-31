# -*- coding: utf-8 -*-
"""grades_analysis.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rSwr9PpRwLJepcrg44lMCodIxkLePx0X
"""

#importation de la bibliotheque numpy
import numpy as np
#creation du tableau "grades"
grades=[85, 90, 88, 92, 95, 80, 75, 98, 89, 83]
#calcul de la moyenne
moyenne_grades=np.mean(grades)
print(f"La moyenne du tableau grades est: {moyenne_grades}")
#calcul de la mediane
    #il faut d'abord trier les notes du tableau grades.
grades.sort()
    #Maintenant nous pouvons calculer la mediane
mediane_grades=np.median(grades)
print(f"La note médiane du tableau grades est : {mediane_grades} ")
#calcul de l'ecart type
ecart_type=np.std(grades)
print(f"L'ecart type du tableau grades est : {ecart_type} ")
#Extraction du maximum
max_grades=np.max(grades)
print(f"la note maximale de grades est : {max_grades} ")
#Extraction du minimum
min_grades=np.min(grades)
print(f"la note minimale de grades est : {min_grades} ")
#fonction numpy pour trier les notes par ordre croissant.
grades=np.sort(grades)
print(grades)
#la fonction numpy pour trouver l'index de la note la plus élevée du tableau.
index_max=np.argmax(grades)
print(f"L'index de la note la plus élevée du tableau est :{index_max} ")
#la fonction numpy pour compter le nombre d'élèves ayant obtenu un score supérieur à 90.
#soit x le nombre d'élèves ayant obtenu un score supérieur à 90.
x=np.sum(grades>90)
print(f"Le nombre d'eleves ayant obtenu un score superieur à 90 est : {x}")
#la fonction numpy pour calculer le pourcentage d'élèves ayant obtenu un score supérieur à 90
#soit y le pourcentage d'élèves ayant obtenu un score supérieur à 90
y=np.mean(grades>90)*100
print(f"le pourcentage d'élèves ayant obtenu un score supérieur à 90 est : {y}%.")
#la fonction numpy pour calculer le pourcentage d'élèves ayant obtenu un score inférieur à 75.
#soit z le pourcentage d'élèves ayant obtenu un score inférieur à 75.
z=np.mean(grades<75)*100
print(f"le pourcentage d'élèves ayant obtenu un score inférieur à 75 est : {z}%.")
#la fonction numpy pour extraire toutes les notes supérieures à 90 et les placer dans un nouveau tableau appelé "high_performers"
# Convertissons la liste en un tableau NumPy
grades_np = np.array(grades)
high_performers = grades_np[grades_np > 90]
print(f"Les notes superieures à 90 sont:{high_performers}")
#Créons un nouveau tableau appelé "passing_grades" qui contient toutes les notes supérieures à 75.
grades_np = np.array(grades)
passing_grades=grades_np[grades_np > 75]
print(f"Les notes superieures à 75 sont:{passing_grades}")