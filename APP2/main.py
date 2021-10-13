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

print(obtenir_qcm())