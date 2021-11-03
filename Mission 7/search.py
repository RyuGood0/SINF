# Fait par Bernard Montens | NOMA : 2333-21-00
def readfile ( filename ):
	""" Crée une liste des lignes contenues dans un fichier dont le nom est ``filename``

	Args:
		filename: le nom d'un fichier de texte
	Retourne:
		une liste dans laquelle chaque ligne du fichier filename est un élément.
		Si filename n'existe pas, la fonction retourne une liste vide.
	"""
	try:
		with open(filename, "r") as f:
			return f.readlines()
	except:
		return []

def get_words ( line ):
	""" pour une chaîne de caractères donnée, retourne une liste des mots dans la chaîne,
		en minuscules, et sans ponctuation, dans l'ordre d'apparence dans le texte.
		Par exemple, pour la chaîne de caractères

		"Turmoil has engulfed the Galactic Republic. The taxation of trade routes
		to outlying star systems is in dispute."

		Le résultat est

		["turmoil", "has", "engulfed", "the", "galactic", "republic", "the",
		"taxation", "of", "trade", "routes", "to", "outlying", "star", "systems",
		"is", "in", "dispute" ]

		Un caractère est considéré comme une ponctuation si ce n'est pas une
		lettre, selon la fonction string.isalpha () .

	Args:
		line: une chaîne de caractères.
	Retourne:
		une liste des mots dans la chaîne, en minuscules, et sans ponctuation.
	"""
	return [''.join(s.lower() if s.isalpha() else '' for s in word) for word in line.split(" ")]

def create_index ( filename ):
	""" crée un index pour le fichier avec nom ``filename``. L'index se compose
		d'un dictionnaire dans lequel pour chaque mot du fichier ``filename``
		on retrouve une liste des indices des lignes du fichier qui contiennent
		ce mot.

		Par exemple, pour un fichier avec le contenu suivant:

		  While the Congress of the Republic endlessly debates
		  this alarming chain of events, the Supreme Chancellor has
		  secretly dispatched two Jedi Knights.

		Une partie de l'index, representé comme dictionnaire, est:


		  {"while": [0], "the": [0,1], "congress": [0], \
		   "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

	Args:
		filename: une chaîne de caractères
	Retourne:
		un dictionnaire avec pour chaque mot du fichier (en minuscules)
		la liste des indices des lignes qui contiennent ce mot.
	"""
	index_dict = {}

	lines = readfile(filename)

	for i in range(len(lines)):
		words = get_words(lines[i])
		for word in words:
			if word not in index_dict:
				index_dict[word] = [i]
			elif i not in index_dict[word]:
				index_dict[word].append(i)

	return index_dict

def get_lines ( words, index ):
	""" Détermine les lignes qui contiennent tous les mots indexes dans ``words``,
		selon l'index ``index``.

		Par exemple, pour l'index suivant:

			index = {"while": [0], "the": [0,1], "congress": [0], 
					"of": [0,1], "republic": [0], ... , "jedi": [2], ...}

		La fonction retourne
			get_lines(["the"]) -> [0,1]
			get_lines(["jedi"]) -> [2]
			get_lines(["the","of"],index) -> [0,1]
			get_lines(["while","the"],index) -> [0]
			get_lines(["congress","jedi"]) -> []
			get_lines(["while","the","congress"]) -> [0]

	Args:
		words: une liste de mots, en minuscules
		index: un dictionnaire contenant pour mots (en minuscules) des listes de nombres entiers
	Retourne:
		une liste des nombres des lignes contenant tous les mots indiqués
	"""

	appearences = []
	for word in words:
		appearences.append(index[word])

	commun_app = []
	for app in appearences:
		if not commun_app:
			commun_app = app
		else:
			sapp = set(app)
			commun_app = sapp.intersection(commun_app)

	return list(commun_app)