def is_adn(s):
	if not s: return False
	for char in s:
		if char.lower() not in ["a", "t", "c", "g"]: return False

	return True

def positions(s, p):
	i = 0
	pos = []
	while i < len(s):
		if s[i:i+len(p)].lower() == p.lower():
			pos.append(i)
			i += len(p)
		else:
			i += 1

	return pos

def distance_h(s, p):
	if len(s) != len(p): return None
	dis = 0
	for i in range(len(s)):
		if s[i].lower() != p[i].lower():
			dis += 1
	return dis

def distances_matrice(l):
	return [[distance_h(l[j], l[i]) for i in range(len(l))] for j in range(len(l))]

print(distances_matrice(["AG", "AT", "GT", "ACG", "ACT"]))