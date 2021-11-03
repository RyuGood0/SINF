# Fait par Bernard Montens | NOMA : 2333-21-00
def readfile(filename): return open(filename).readlines() if __import__("os").path.exists(filename) else []
def get_words(line): return [''.join(s.lower() if s.isalpha() else '' for s in word) for word in line.split(" ")]
def create_index(filename): return {key: [j for j in range(len(readfile(filename))) if key in get_words(readfile(filename)[j])] for sublist in [[word for word in get_words(readfile(filename)[i])] for i in range(len(readfile(filename)))] for key in sublist}
def get_lines(words, index): return list(set(index[words[0]]).intersection(*[set(index[word]) for word in words]))

print(get_lines(["the", "of", "while"], create_index("text_example_1.txt")))