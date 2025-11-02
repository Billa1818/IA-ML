import numpy as np # Importation de la bibliothèque NumPy
tab=np.linspace(0,360,50)
print("Tableau des angles en degrés :\n", tab) # Affichage du tableau des angles en degrés
cos=np.cos(tab)
print("Cosinus des angles :\n", cos) # Affichage du cosinus des angles
sin=np.sin(tab)
print("Sinus des angles :\n", sin) # Affichage du sinus des angles
tan=np.tan(tab)
print("Tangente des angles :\n", tan) # Affichage de la tangente
# angle avec sin > 0.9
angles_sin_09 = tab[sin > 0.9]
print("Angles avec sin > 0.9 :\n", angles_sin_09) # Affichage des angles avec sin > 0.9
# angle avec cos < -0.5
angles_cos_moins05 = tab[cos < -0.5]
print("Angles avec cos < -0.5 :\n", angles_cos_moins05) # Affichage des angles avec cos < -0.5
# angle avec |tan|>2 
angles_tan_2 = tab[np.abs(tan) > 2]
print("Angles avec |tan| > 2 :\n", angles_tan_2) # Affichage des angles avec |tan| > 2