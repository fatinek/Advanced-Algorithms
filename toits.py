import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.patches import Rectangle

immeubles_tests = [(13,3,8),(5,3,9),(19,4,12),(3,4,5),(10,7,5),(7,2,4),(1,2,5),(21,7,12)]

# Dimensionnement de la fenêtre
def initialisation(n):
	plt.figure(n)
	plt.xlim([0,30])
	plt.ylim([0,20])

def dessiner_immeubles(immeubles):
	ax = plt.gca()
	for (x,w,h) in immeubles:
		ax.add_patch(Rectangle((x,0), w, h,fill=None,linewidth=5))

def dessiner_ligne(ligne):
	ax = plt.gca()
	X,Y=0,0
	for (x,y) in ligne:
		# X Y -> x Y -> x y
		ax.add_line(lines.Line2D([X,x,x], [Y,Y,y], linewidth=1, color='red'))
		X=x
		Y=y
		
		
# Pour visualiser un résultat :
# 	Initialisation(1)
#	dessiner_immeubles(liste_immeubles) 
#	dessiner_ligne(ligne_de_toits)
#	plt.show()
# L'appel a "plt.show()" bloque le code. L'execution continue lorsqu'on ferme la fenetre graphique.



# ---------------
# PREMIERE PARTIE
# ---------------

def ajouter_immeuble(ligne,immeuble):
	(x,w,h) = immeuble	

	resultat = []
	i=0
	
	# Tant qu'on est a gauche de l'immeuble
	while i < len(ligne) and ligne[i][0] < x:
		# On insère l'ancienne ligne dans la nouvelle ligne jusqu'à arriver à l'immeuble
		resultat.append(ligne[i])
		i = i+1
		#--------------
		
	# Ajout du mur de gauche si besoin
	if i < len(ligne):
		# Si le mur est a la meme abscisse qu'un autre
		if x == ligne[i][0]:
			y_avant = ligne[i][1]
			y_apres = max(h, ligne[i][1])
			if (y_avant != y_apres):
				resultat.append([x,y_apres])
			i = i+1
		else:
			# Si y_immeuble > y_avant
			if h > ligne[i][1]:
				resultat.append([x,h])
			#--------------
	else:
		# On est à l'extérieur de l'ancienne ligne, donc il suffit simplement d'ajouter l'immeuble
		resultat.append([x,h])
		resultat.append([x+w,0])
		#--------------

		
	# Tant qu'on est a l'interieur de l'immeuble
	while i < len(ligne) and ligne[i][0] < x+w:
		# On calcule les hauteurs avant et après le point
		y_apres = max(h, ligne[i][1])
		y_avant = max(h, ligne[i-1][1])
		if (y_avant != y_apres):
			resultat.append([ligne[i][0], y_apres)
		i = i+1
		#--------------

	# Ajout du mur droit
	if i < len(ligne):
		# Meme abscisse qu'un autre mur
		if x+w == ligne[i][0]:
			#--------------
			# Quelque chose
			#--------------
		else:
			#--------------
			# Quelque chose
			#--------------
	else:
		#--------------
		# Quelque chose
		#--------------

	# Tant qu'on est a droite de l'immeuble
	while i < len(ligne):
		#--------------
		resultat.append(ligne[i])
		i = i+1
		#--------------

	return resultat

	
	
	
# ---------------
# DEUXIEME PARTIE
# ---------------

def fusion_lignes(l1,l2):
	resultat=[(0,0)]

	#--------------
	# Quelque chose
	#--------------
	
	return resultat


def creer_ligne(immeubles):
	# Cas de base
	if True: # A changer...
		ligne = []
		#--------------
		# Quelque chose
		#--------------
		return ligne
	# Cas general
	else:
		# Separation en deux sous-problemes
		#--------------
		# Quelque chose
		#--------------
		
		# Resolution des sous-problemes
		#--------------
		# Quelque chose
		#--------------

		# Fusion
		#--------------
		# Quelque chose
		#--------------

		ligne = []
		return ligne

#-------------------------
# TEST DIVISER POUR REGNER
#-------------------------

#initialisation(1)
#dessiner_immeubles(immeubles)
#L=creer_ligne(immeubles)
#dessiner_ligne(L)
#plt.show()
