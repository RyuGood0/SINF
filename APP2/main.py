def prng(seed, max):
	while True:
		seed = seed ^ 6511146
		seed = (seed*3644) % 852693
		seed = seed*85225
		seed = seed % 352368
		yield seed % max

def mode_de_cotation():
	while True:
		mode = input("Veuillez choisir votre mode de cotation :\n\t1. Cool (Une mauvaise réponse n'engage rien)\n\t2. Sévère (Une mauvaise réponse enlève 1 point)\n")
		if mode in ["1", "2"]:
			break

	return mode

def obtenir_qcm():
	fichier = input("Veuillez entrer le nom du fichier contenant le QCM: ")
	try:
		f = open(fichier, "r")
		return fichier
	except:
		print("Il semblerait que le fichier soit invalide, veuillez vérifier puis réessayer")
		exit(1)

from time import time
def shuffle(l):
	temp_l = l.copy()
	randomised_l = []
	while len(randomised_l) != len(l):
		ran_index = next(prng(int(time()*100), len(temp_l)))
		
		randomised_l.append(temp_l[ran_index])
		temp_l.pop(ran_index)

	return randomised_l

print(shuffle([1, 2, 3, 4, 5]))

from qcm import build_questionnaire
def donner_qcm():
	mode = mode_de_cotation()
	fichier = obtenir_qcm()
	questions = build_questionnaire(fichier)
	
	randomised_questions = shuffle(questions)

	réponses = poser_questions(randomised_questions)

	cote = coter(réponses, randomised_questions, mode)
	max_cote = obtenir_cote_max(randomised_questions)
	print(f"Vous avez obtenu {cote}/{max_cote}!")

def poser_questions(questions):
	answers = []
	print('Plusieurs réponses possibles, séparez-les par un ","')
	for question in questions:
		while True:
			input_str = question[0]
			for i in range(len(question[1])):
				input_str += f"\n\t{i+1}. {question[1][i][0]}"
			answer = input(input_str + "\n")
			if len(answer) == 1 and answer in [str(num) for num in list(range(1, len(question[1])+1))]:
				break
			else:
				valid = True
				for ans in answer.replace(" ", "").split(","):
					if ans not in [str(num) for num in list(range(1, len(question[1])+1))]:
						valid = False
				if valid:
					break
					
		answers.append(answer.replace(" ", "").split(","))

	return answers

def obtenir_cote_max(questions):
	max_cote = 0
	for question in questions:
		trues = sum(x.count(True) for x in question[1])
		max_cote += trues
	return max_cote

def coter(réponses, questions, mode):
	cote = 0
	for i in range(len(réponses)):
		if len(réponses[i]) == 1:
			if questions[i][1][int(réponses[i][0])-1][1] == True:
				cote += 1
			elif mode == "2":
				cote -= 1
		else:
			for réponse in réponses[i]:
				if questions[i][1][int(réponse)-1][1] == True:
					cote += 1
				elif mode == "2":
					cote -= 1
	
	return cote
