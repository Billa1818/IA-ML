import numpy as np # Importation de la bibliothèque NumPy
mat12x12=np.arange(1,145).reshape(12,12) # Création d'un tableau 12x12 avec des entiers de 1 à 144
print("Tableau original :\n", mat12x12) # Affichage du tableau
matdiv4=np.vsplit(mat12x12,4) # Division du tableau en 4 sous-tableaux égaux le long de l'axe vertical
# creation des quadiants
q1=np.hsplit(matdiv4[0],2) # Division du premier sous-tableau en deux parties égales le long de l'axe horizontal
q2=np.hsplit(matdiv4[1],2) # Division du deuxième sous-tableau en deux parties égales le long de l'axe horizontal
q3=np.hsplit(matdiv4[2],2) # Division du troisième sous-tableau en deux parties égales le long de l'axe horizontal
q4=np.hsplit(matdiv4[3],2) # Division du quatrième sous-tableau en deux parties égales le long de l'axe horizontal
quadf1=np.vstack((q1[0],q2[0])) # Création du premier quadrant en empilant verticalement les premières moitiés des deux premiers sous-tableaux
quadf2=np.vstack((q1[1],q2[1])) # Création du deuxième quadrant en empilant verticalement les deuxièmes moitiés des deux premiers sous-tableaux
quadf3=np.vstack((q3[0],q4[0])) # Création du troisième quadrant en empilant verticalement les premières moitiés des deux derniers sous-tableaux
quadf4=np.vstack((q3[1],q4[1])) # Création du quatrième quadrant en empilant verticalement les deuxièmes moitiés des deux
# Reconstruction du tableau original à partir des quadrants
mat_reconstruit=np.vstack((np.hstack((quadf4,quadf2)),np.hstack((quadf3,quadf1))))
print("Tableau reconstruit :\n", mat_reconstruit) # Affichage du tableau reconstruit