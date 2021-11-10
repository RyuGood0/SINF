# Fait par Bernard Montens | NOMA : 2333-21-00
def readfile(filename): return [line.replace("\n", "") for line in open(filename).readlines()] if __import__("os").path.exists(filename) else []
def get_words(line): return [alphaword for alphaword in [''.join(s.lower() if s.isalpha() else '' for s in word) for word in line.split(" ")] if alphaword]
def create_index(filename): return {key: [j for j in range(len(readfile(filename))) if key in get_words(readfile(filename)[j])] for sublist in [[word for word in get_words(readfile(filename)[i])] for i in range(len(readfile(filename)))] for key in sublist}
def get_lines(words, index): 
    try: return list(set(index[words[0]]).intersection(*[set(index[word]) for word in words])) 
    except: return []