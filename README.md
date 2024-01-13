# cna-mughal-history
A computational perspective on character networks through the works of Mughal historians.

# Files
* `humayunnama.txt`: The text of Gulbadan Begam's *Humayunnama*, taken from [the Packard Humanities page](https://persian.packhum.org/main). This has been postprocessed by:
    - removing `>graphic<`s and the associated captions
    - resolving linebreaks within words, *e.g.*, `Compass-\nionate` => `Compassionate`
    - removing page marks e.g. `(3b)` [`\(\d+\w\)`]
    - removing asterisks
* `names.txt`