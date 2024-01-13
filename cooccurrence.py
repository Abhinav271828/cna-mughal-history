from nltk.tokenize import word_tokenize
from nltk.corpus import words, stopwords
from tqdm import tqdm

f = open('humayunnama.txt', 'r')
w = []
for line in tqdm(f):
    w += word_tokenize(line)
f.close()

names = []
i = 0
while i < len(w):
    if w[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and w[i].lower() not in stopwords.words('english'):
        name = []
        while w[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ'" and w[i] != "'s" or w[i][:2] == "u-":
            name += [w[i]]
            i += 1
        names.append(name)
    i += 1

names = [[word for word in n if word.lower() not in words.words()] for n in tqdm(names)]
names = [name for name in names if name != []]

g = open('names.txt', 'a')
#g.write("\n".join(map(" ".join,names)))
g.writelines(map(" ".join,names))
g.close()