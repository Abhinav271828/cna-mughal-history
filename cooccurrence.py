from nltk.tokenize import word_tokenize
from nltk.corpus import words, stopwords
from tqdm import tqdm
from collections import defaultdict

# Extract and tokenize file contents
f = open('humayunnama.txt', 'r')
w = []
for line in tqdm(f):
    w += word_tokenize(line)
f.close()

# Get list of names and places where they occur
occurrences = defaultdict(lambda : [])
i = 0
while i < len(w):
    if w[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and w[i].lower() not in stopwords.words('english'):
        name = []
        pos = i
        while w[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ'" and w[i] != "'s" or w[i][:2] == "u-":
            name += [w[i]]
            i += 1
        occurrences[tuple(name)].append(pos)
    i += 1

occurrences = {tuple(word for word in n if word.lower() not in words.words()) : occurrences[n] for n in tqdm(occurrences.keys(), desc='Filtering English words')}
occurrences = {n : occurrences[n] for n in occurrences if n != tuple()}
occurrences = {" ".join(n) : occurrences[n] for n in occurrences}
names = list(occurrences.keys())

W = 5
cooccurrence = {}
for i in tqdm(range(len(names)), desc="Extracting cooccurrences"):
    name1 = names[i]
    positions1 = occurrences[name1]
    for name2 in names[:i] + names[i+1:]:
        positions2 = occurrences[name2]
        distances = [abs(p1 - p2) for p1 in positions1 for p2 in positions2]
        cooccurrence[(name1, name2)] = sum(1 for d in distances if d <= W)