from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import words, stopwords
from tqdm import tqdm
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import pickle

try:
    with open('humayunnama_occ.pickle', 'rb') as handle:
        occurrences = pickle.load(handle)
except:
    # Extract and tokenize file contents
    f = open('humayunnama.txt', 'r')
    w = []
    for line in tqdm(f, desc="Tokenizing"):
        sentences = sent_tokenize(line)
        for s in sentences:
            ws = word_tokenize(s)
            ws = [word.replace('(', '').replace(')', '').replace('.', '') for word in ws]
            ws = [word[:word.index('—')] if '—' in word else word for word in ws]
            w += [word for word in ws if word != ''] + ['<//>']
    f.close()

    # Get list of names and places where they occur
    occurrences = defaultdict(lambda : [])
    i = 0
    while i < len(w):
        if w[i][0] in "AĀBCDEFGHḤIJKLMNOPQRSṢTUŪVWXYZẔ" and w[i].lower() not in stopwords.words('english'):
            name = []
            beg = i
            while i < len(w) and \
                 (w[i][0] in "AĀBCDEFGHḤIJKLMNOPQRSṢTUŪVWXYZẔ" and w[i] != "'s" or \
                  w[i][:2] == "u-" or \
                  w[i] == "'" or w[i][:2] == "l-" or \
                  w[i] == "a" or \
                  w[i][0] == '-' or i > 0 and w[i-1][-1] == '-'):
                name += [w[i]]
                i += 1
            occurrences[tuple(name)].append((beg, i))
        i += 1

    occurrences = {tuple(word for word in n if word.lower == "beg" or word.lower() not in ["meantime"] + words.words()) : occurrences[n] for n in tqdm(occurrences.keys(), desc='Filtering English words')}
    occurrences = {n : occurrences[n] for n in occurrences if n != tuple()}
    occurrences = {" ".join(n) : occurrences[n] for n in occurrences}
    with open('humayunnama_occ.pickle', 'wb') as handle:
        pickle.dump(occurrences, handle, protocol=pickle.HIGHEST_PROTOCOL)

try:
    with open('people.txt', 'r') as f:
        print("Found people.txt, using.")
        all_names = []
        names = []
        mapping = {}
        for line in f:
            n = line[:-1].split(':')
            all_names += n
            names.append(n[0])
            print(names)
            if len(n) > 1:
                for name in n[1:]:
                    mapping[name] = n[0]
        
    for name in all_names:
        if name in mapping:
            print(f"Shifting {name} to {mapping[name]}")
            occurrences[mapping[name]] += occurrences[name]
            del occurrences[name]
            

except FileNotFoundError:
    names = list(occurrences.keys())
    with open('names.txt', 'r') as f:
        for name in names: f.write(f"{name}\n")
    print("Using names including non-people!")

# For all pairs of words, find the number of times they occur within W words of each other.
W = 5
cooccurrence = {}
for i in tqdm(range(len(names)), desc="Extracting cooccurrences"):
    name1 = names[i]
    positions1 = occurrences[name1]
    for name2 in names[:i] + names[i+1:]:
        positions2 = occurrences[name2]
        distances = [min(abs(b1-e2), abs(b2-e1)) for b1, e1 in positions1 for b2, e2 in positions2]
        cooccurrence[(name1, name2)] = sum(1 for d in distances if d <= W)

# Collapse name1-name2 and name2-name1
for (n1, n2) in [(n1, n2) for n1 in names for n2 in names]:
    if (n1 <= n2): continue
    cooccurrence[(n2, n1)] += cooccurrence[(n1, n2)]
    del cooccurrence[(n1, n2)]

# Construct graph
G = nx.Graph()
G.add_nodes_from(names)
for (n1, n2) in cooccurrence:
    if cooccurrence[(n1, n2)] > 0:
        G.add_edge(n1, n2)

# Remove nodes without edges
for n in names:
    if len(G.edges(n)) == 0:
        G.remove_node(n)

components = [G.subgraph(c).copy() for c in sorted(nx.connected_components(G), key=len, reverse=True)]

for component in components[:1]:
    nx.draw(component, nx.spring_layout(component), node_size=2, with_labels=True, font_size=5)
    plt.show()