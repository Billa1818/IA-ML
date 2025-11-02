import numpy as np

original = np.arange(25).reshape(5, 5)
print("Tableau original :\n", original)

# Vue
vue = original[1:4, 1:4]
print("\nVue créée")
print(f"vue.base is original : {vue.base is original}")
print(f"Vue est une copie : {vue.flags['OWNDATA']}")

# Copie
copie = original.copy()
print(f"\ncopie.base is original : {copie.base is original}")
print(f"Copie possède ses données : {copie.flags['OWNDATA']}")

# Modifications
vue[0, 0] = 999
copie[0, 0] = 777

print("\nAprès modification de la vue :")
print("Original :\n", original)
print("\nAprès modification de la copie :")
print("Copie :\n", copie)
print("Original inchangé par la copie")

