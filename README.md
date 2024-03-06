# cna-mughal-history
A computational perspective on character networks through the works of Mughal historians.

# Text Files
* `humayunnama.txt`: The text of Gulbadan Begam's *Humayunnama*, taken from [the Packard Humanities page](https://persian.packhum.org/main). This has been postprocessed by:
    - removing `>graphic<`s and the associated captions
    - resolving linebreaks within words, *e.g.*, `Compass-\nionate` => `Compassionate`
    - removing page marks e.g. `(3b)` [`\(\d+\w\)`]
    - removing asterisks
* `names.txt`: A list of occurrences of various names (people and places) in the *Humayunnama*. All contiguous sequences of words beginning with capital letters were extracted. To account for names like `Badī'u-z-zamān`, the token `'` and all tokens starting with `u-` were also included. English words were filtered out of the final list (*e.g.*, `New Year's Garden`).

# Images
* `only_people.png`: The largest connected component in the co-occurrence graph (unweighted) of all characters. The window size is 5.
* `top_centrality.png`: The same graph, but taking only the nodes with centrality ≥ 0.02.