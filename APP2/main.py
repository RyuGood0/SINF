def prng(seed, max):
	while True:                         # On prend le seed et on le modifie avec des opérations, pour s'assurer qu'une petite modification
		seed = seed ^ 6511146           # fasse de grands changements
		seed = (seed*3644) % 852693
		seed = seed*85225
		seed = seed % 352368
		yield seed % max                # On return le seed modifié en modolo "max" pour avoir un nombre entre 0 et max

def mode_de_cotation():
	while True:                         # On demande simplement à l'utilisateur de choisir un mode et si l'input n'est pas valide, on redemande
		mode = input("Veuillez choisir votre mode de cotation :\n\t1. Cool (Une mauvaise réponse n'engage rien)\n\t2. Sévère (Une mauvaise réponse enlève 1 point)\n\t3. Anti-hasard (Quelqu'un qui répond aléatoirement sera pénalisé)\n\t4. Mode évaluation : affiche les résultats de chaque mode\n>> ")
		if mode in ["1", "2", "3", "4"]:
			break

	return mode

def obtenir_qcm():
	fichier = input("Veuillez entrer le nom du fichier contenant le QCM: ")
	try:                                 # On demande un fichier. S'il existe, on le return, sinon on dit qu'il est invalide
		f = open(fichier, "r")
		return fichier
	except:
		print("Il semblerait que le fichier soit invalide, veuillez vérifier puis réessayer")
		exit(1)

from time import time
def shuffle(l):
	temp_l = l.copy()                    # On utilise la fonction PRNG pour mélanger la liste "l" aléatoirement
	randomised_l = []
	while len(randomised_l) != len(l):
		ran_index = next(prng(int(time()*100), len(temp_l)))
		
		randomised_l.append(temp_l[ran_index])
		temp_l.pop(ran_index)

	return randomised_l

from qcm import build_questionnaire
def donner_qcm():
	mode = mode_de_cotation()            # On regroupe toutes les fonctions pour donner le QCM
	fichier = obtenir_qcm()
	questions = build_questionnaire(fichier)
	
	randomised_questions = shuffle(questions)

	réponses = poser_questions(randomised_questions)

	if mode == "4":
		modes = ["Cool", "Sévère", "Anti-hasard"]
		for i in range(1, 4):
			cote, max_cote = coter(réponses, randomised_questions, str(i))
			print(f"Vous avez obtenu {cote}/{max_cote} en mode {modes[i-1]}!")
	else:		
		cote, max_cote = coter(réponses, randomised_questions, mode)
		print(f"Vous avez obtenu {cote}/{max_cote}!")

def poser_questions(questions):
	answers = []                          # On print les questions avec chacune de leur réponses
	print('Plusieurs réponses possibles, séparez-les par un ","')
	for question in questions:
		while True:
			input_str = question[0]
			for i in range(len(question[1])):
				input_str += f"\n\t{i+1}. {question[1][i][0]}"
			answer = input(input_str + "\n>> ")
			if len(answer) == 1 and answer in [str(num) for num in list(range(1, len(question[1])+1))]:
				break
			else:                          # On s'assure que la réponse de l'utilisateur est dans les réponses possibles
				valid = True
				for ans in answer.replace(" ", "").split(","):
					if ans not in [str(num) for num in list(range(1, len(question[1])+1))]:
						valid = False
				if valid:
					break
					
		answers.append(answer.replace(" ", "").split(","))

	return answers

def obtenir_cote_max(questions):
	max_cote = 0                           # On compte simplement le nombre de bonnes réponses possibles
	for question in questions:
		trues = sum(x.count(True) for x in question[1])
		max_cote += trues
	return max_cote

def obtenir_reponses_totales(questions):
	reponses_tot = 0                       # On compte le nombre total de réponses
	for question in questions:
		reponses_tot += len(question[1])
	return reponses_tot

def coter(réponses, questions, mode):
	cote = 0                               # On cote l'utilisateur dépendant de ses réponses
	for i in range(len(réponses)):
		if len(réponses[i]) == 1:
			if questions[i][1][int(réponses[i][0])-1][1] == True:
				cote += 1
			elif mode == "2":              # Si la réponse est fausse, on retire 1 point uniquement si le mode de cotation est "Sévère"
				cote -= 1
		else:
			for réponse in réponses[i]:
				if questions[i][1][int(réponse)-1][1] == True:
					cote += 1
				elif mode == "2":
					cote -= 1

	max_cote = obtenir_cote_max(questions)

	if mode == "3":                         # Si le mode de cotation est "Anti-hasard", on calcule la moyenne statistique du QCM 
		moyen_stat = round(obtenir_cote_max(questions)/obtenir_reponses_totales(questions) * obtenir_cote_max(questions))
		if cote == moyen_stat:              # On compare la cote de l'utilisateur et la moyenne et si elles sont égales, on lui donne 0
			cote = 0
	
	return cote, max_cote

donner_qcm()