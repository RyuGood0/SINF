def is_correct(PRNG):
    samples = []
    for seed in range(11):
        r = PRNG(seed, 11)

        valeurs = []
        seen = []
        for i in range(1000):
            valeur = next(r)
            if valeur not in list(range(11)): return False
            if valeur not in seen:
                seen.append(valeur)
            valeurs.append(valeur)

        if len(seen) != 11:
            return False
        samples.append(valeurs[:100])
        
    for i in range(len(samples)):
        for j in range(len(samples)):
            if i==j: continue
            if samples[i] == samples[j]: return False
            
    return is_cycle(samples[0])

def is_cycle(samples):
    samples.reverse()
    first_value_indices = [index for index, value in enumerate(samples) if value==samples[0]]
    
    chunks = [samples[first_value_indices[i]:first_value_indices[i+1]] for i in range(len(first_value_indices)-2)]
    
    return not all(x==chunks[0] for x in chunks)