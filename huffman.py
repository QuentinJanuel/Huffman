# Implementation des arbres
class Arbre:
	def __init__(self, lettre=None, occurences=None):
		self.gauche  = None
		self.droite = None
		self.lettre = lettre
		self.occurences = occurences

# Texte a compresser
texte = """
On peut ici s'amuser a remplir un long texte,
ce n'est pas un probleme.
Notre algorithme le compresse parfaitement bien
"""

# Liste des arbres
arbres = []

# Remplissage des arbres
texte_temporaire = texte
while len(texte_temporaire) > 0:
	# On recupere la premiere lettre
	lettre = texte_temporaire[0]
	# On compte le nombre de fois qu'elle est dans le texte
	occurences = texte_temporaire.count(lettre)
	# On la supprime du texte
	texte_temporaire = texte_temporaire.replace(lettre, "")
	# On la rajoute dans les arbres
	arbres.append(Arbre(lettre, occurences))

# Une fonction pour trier par occurence la liste des arbres
def ordre(arbre):
	return arbre.occurences

# On repete jusqu'a ce qu'il ne reste plus qu'un arbre
while len(arbres) > 1:
	# On trie les arbres en mettant les arbres
	# les plus frequentes au debut
	arbres.sort(key=ordre, reverse=True)
	# On recupere les deux derniers arbres
	arbre1 = arbres.pop()
	arbre2 = arbres.pop()
	# On compte les occurences cumulees des deux
	occurences = arbre1.occurences+arbre2.occurences
	# On cree un arbre qui sera la composition des deux sous arbres
	arbre = Arbre("", occurences)
	arbre.gauche = arbre1
	arbre.droite = arbre2
	# On le rajoute dans la liste
	arbres.append(arbre)

# On a cree notre arbre en fonction du texte :
# c'est le seul qui reste dans notre liste d'arbres
arbre = arbres[0]

# Une fonction qui rend le code d'une lettre suivant l'arbre
def codeLettreArbre(lettre, arbre):
	# Si l'arbre n'existe pas, ce n'est pas possible
	if arbre == None:
		return ("", False)
	# Si la lettre est la bonne, c'est possible
	if arbre.lettre == lettre:
		return ("", True)
	# On calcule recursivement le code du sous arbre gauche
	# et celui du sous arbre droit
	gauche = codeLettreArbre(lettre, arbre.gauche)
	droite = codeLettreArbre(lettre, arbre.droite)
	# Si c'est possible a gauche,
	# on rend un 0 suivi du reste du code en partant de la gauche
	if gauche[1]:
		return ("0"+gauche[0], True)
	# Si c'est possible a droite,
	# on rend un 1 suivi du reste du code en partant de la droite
	if droite[1]:
		return ("1"+droite[0], True)
	# Si ce n'est possible ni a droite ni a gauche
	# ce n'est pas possible
	return ("", False)

# Creation du code
code = ""
texte_temporaire = texte
while len(texte_temporaire) > 0:
	# On recupere la premiere lettre
	lettre = texte_temporaire[0]
	# On la supprime du texte
	texte_temporaire = texte_temporaire[1:]
	# On recupere le code de cette lettre
	lettre_code = codeLettreArbre(lettre, arbre)
	# On ajoute son code au code total
	code += lettre_code[0]

print(code)
