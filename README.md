# cna-mughal-history
A computational perspective on character networks through the works of Mughal historians.

# Text Files
* `humayunnama.txt`: The text of Gulbadan Begam's *Humayunnama*, taken from [the Packard Humanities page](https://persian.packhum.org/main). This has been postprocessed by:
    - removing `>graphic<`s and the associated captions
    - resolving linebreaks within words, *e.g.*, `Compass-\nionate` => `Compassionate`
    - removing page marks e.g. `(3b)` [`\(\d+\w\)`]
    - removing asterisks
* `names.txt`: A list of occurrences of various names (people and places) in the *Humayunnama*. We use [the spaCy module](https://spacy.io) to perform NER (named entity recognition) and use the names tagged as `PERSON` or `ORG`.
* `people.txt`: A list of names (not occurrences) of people in the *Humayunnama*. Manually filtered from `names.txt`.

# Images
* `only_people.png`: The largest connected component in the co-occurrence graph (unweighted) of all characters. The window size is 5.
* `top_centrality.png`: The same graph, but taking only the nodes with centrality ≥ 0.02.
* `centrality_and_distance.png`: The centrality of each person (blue) and the distance of that person's embedding from Humayun's (orange).