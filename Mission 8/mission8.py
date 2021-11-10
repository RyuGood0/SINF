class Duree :
	def __init__(self, h, m, s):
		"""
		@pre: h, m et s sont des entiers positifs (ou zéro)
			m et s sont < 60
		@post: Crée une nouvelle durée en heures, minutes et secondes.
		"""
		self.h = h
		self.m = m
		self.s = s

	def to_secondes(self):
		"""
		@pre:  -
		@post: Retourne le nombre total de secondes de cette instance de Duree (self).
		Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
		"""
		return self.h*3600 + self.m*60 + self.s

	def delta(self, d):
		"""
		@pre:  d est une instance de la classe Duree
		@post: Retourne la différence en secondes entre cette durée (self)
			et la durée d passée en paramètre.
			Cette valeur renovoyée est positif si cette durée (self)
			est plus gramd que la durée d, négatif sinon.
		Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
		et la durée d est 0h 1m 25s, la valeur retournée est 31200.
		Inversement, si cette durée (self) est 0h 1m 25s et la durée
		d est 8h 41m 25s, alors la valeur retournée est -31200.
		"""
		return self.to_secondes() - d.to_secondes()

	def apres(self,d):
		"""
		@pre:  d est une instance de la classe Duree
		@post: Retourne True si cette durée (self) est plus grand que la durée
			d passée en paramètre; retourne False sinon.
		"""
		return self.to_secondes() > d.to_secondes()

	def ajouter(self,d):
		"""
		@pre:  d est une instance de la classe Duree
		@post: Ajoute une autre durée d à cette durée (self),
			corrigée de manière à ce que les minutes et les secondes soient
			dans l'intervalle [0..60[, en reportant au besoin les valeurs
			hors limites sur les unités supérieures
			(60 secondes = 1 minute, 60 minutes = 1 heure).
			Ne retourne pas une nouvelle durée mais modifié la durée self.
		"""
		self.h += d.h
		self.m += d.m
		self.s += d.s
		if self.s >= 60:
			self.m += self.s // 60
			self.s %= 60
		if self.m >= 60:
			self.h += self.m // 60
			self.m %= 60

	def __repr__(self):
		"""
		@pre:  -
		@post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
		Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
		retourne le String désiré avec les nombres en deux chiffres en ajoutant
		les zéros nécessaires.
		"""
		return f"{self.h:02}:{self.m:02}:{self.s:02}"

class Chanson :
	def __init__(self,t,a,d):
		"""
		@pre:  t et a sont des string, d est une instance de la classe Duree
		@post: Crée une nouvelle chanson, caractérisée par un titre t,
				un auteur a et une durée d.
		"""
		self.titre = t
		self.auteur = a
		self.duree = d

	def __repr__(self):
		"""
		@pre:  -
		@post: Retourne un string décrivant cette chanson sous le format
			"TITRE - AUTEUR - DUREE".
			Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
		"""
		return f"{self.titre} - {self.auteur} - {self.duree}"
	
class Album :
	def __init__(self, numero):
		"""
		@pre:  numero est un entier identifiant de facon unique cet album
		@post: Crée un nouvel album, avec comme identifiant le numero,
			et avec une liste de chansons vide.
		"""
		self.numero = numero
		self.chansons = []
		self.duree = Duree(0,0,0)

	def add(self,chanson):
		"""
		Cette méthode retourne False et ne modifie rien si lors de l'ajout de la chanson l'album aurait atteint 100 chansons ou sa durée aurait dépassé 75 minutes. Sinon la chanson est rajoutée à la fin de la liste des chansons de cet album, la durée totale de l'album est augmentée avec la durée de la chanson, et la méthode add retourne True.
		"""

		if len(self.chansons) >= 100 or self.duree.to_secondes() + chanson.duree.to_secondes() > 75*60:
			return False
		else:
			self.chansons.append(chanson)
			self.duree.ajouter(chanson.duree)
			return True

	def __repr__(self):
		"""
		Finalement, implémentez la méthode de conversion __str__ pour imprimer la description d'un album selon le format suivant:

		Album 21 (12 chansons, 00:47:11)
		01: White_Wedding - Billy_Idol - 00:04:12
		02: Stand_And_Deliver - Adam_&_The_Ants - 00:03:33
		03: You_Spin_Me_Around - Dead_Or_Alive - 00:03:14
		04: Wired_For_Sound - Cliff_Richard - 00:03:38
		05: Some_Like_It_Hot - The_Power_Station - 00:03:45
		06: 99_Luftballons - Nena - 00:03:50
		07: Keep_On_Loving_You - Reo_Speedwagon - 00:03:22
		08: Seven_Into_The_Sea - In_Tua_Nua - 00:03:51
		09: Love_Is_A_Battlefield - Pat_Benatar - 00:05:20
		10: Etienne - Guesch_Patti - 00:04:07
		11: This_Is_Not_A_Love_Song - Public_Image_Limited - 00:04:12
		12: Love_Missile_F1-11 - Sigue_Sigue_Sputnik - 00:04:07
		"""

		s = f"Album {self.numero} ({len(self.chansons)} chansons, {self.duree})\n"
		for i, chanson in enumerate(self.chansons):
			s += f"{i+1}: {chanson} \n"
		return s

if __name__ == "__main__":
	"""
	lit dans le fichier music-db.txt, ligne par ligne, des descriptifs de chanson au format décrit en tête de cette section;
	pour chaque ligne lue, construite une instance de Chanson;
	stocke ses chansons dans un album avec identifiant le numéro 1;
	lorsque le nombre de chansons stockés dans cet album a atteint 100 chansons ou la durée dépasserait 75 minutes, imprime à la console un descriptif de cet album avec les chansons accumulées, suivant l'exemple donné ci-dessus;
	poursuit la lecture du fichier et l'ajout des chansons dans un album suivant (incrémentez le numéro identifiant l'album de 1 pour chaque nouvel album);
	répète ces étapes jusqu'à ce que le fichier est vide et imprime le dernier album.
	"""

	album = Album(1)
	with open("music-db.txt", "r") as f:
		for ligne in f:
			ligne = ligne.strip()
			titre, auteur, minutes, secondes = ligne.split(" ")

			duree = Duree(0,int(minutes),int(secondes))
			chanson = Chanson(titre,auteur,duree)
			if album.add(chanson):
				continue
			else:
				print(album)
				album = Album(album.numero+1)
				album.add(chanson)
	print(album)