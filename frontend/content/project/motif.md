+++
title = "Finding Hidden Messages In DNA"

date = 2018-12-05T15:53:10-08:00
lastmod = 2018-12-05T15:53:10-08:00
draft = false

tags = ["python", "bioinformatics"]
summary = "Las Vegas Algorithms to the rescue!"

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = "motif.png"

[header]
image = "motif.png"

+++

This past year I have been extremely interested in getting more hands on expierence with Bioinformatics.
I decided to try the Bioinformatics specialization on Coursera presented by UCSD.
The over all goal of the first class in the sequence was to find motifs in dna.
By the end of the class I implemented many different motif finding algorithms in python,
and found a Las Vegas Algorithm (Random Motif Search) to surprisingly be one of the most efficient.

# First, what is a motif?
"Sequence motifs are short, recurring patterns in DNA that are presumed to have a biological function. 
Often they indicate sequence-specific binding sites for proteins such as nucleases 
and transcription factors (TF). Others are involved in important processes at the 
RNA level, including ribosome binding, mRNA processing (splicing, editing, 
polyadenylation) and transcription termination." - Nature

# What does that mean in lay-mans terms:
It means that among several sequences of dna, we are looking for a certain pattern.
The tough part is that we don't know what the pattern is initially, 
and that the pattern may not exactly match its counterparts in other DNA strings.

# So how does a Las Vegas Algorithm help?
If you don't know, a Las Vegas algorithm is a randomized algorithm that always gives a correct result.
In our case we will randomly choose motifs (or substrings of length k in the dna) and compare them to other randomly computed motifs from the dna.
Then we will continuously compute a Profile Matrix (a matrix defining the probability of each nucleotide occuring in the motif), generate a new collection of motifs hoping to find a better and better score.

The following algorithm would be run thousands of times, in order to find a good result. The more times it is run, the more likely it is to coalesce around the correct motif.

```python

def randomized_motif_search(k, t, dna):
    """
    Input: Integers k and t, and collection of strings Dna.
    :return: best motifs
    """

    bestMotifs = random_motifs(dna, k)
    bestScore = score_motifs(bestMotifs)
    while True:
        profile = profile_from_motifs(bestMotifs)
        motifs = motifs_from_profile(dna, profile)
        score = score_motifs(motifs)
        if score < bestScore:
            bestMotifs = motifs
            bestScore = score
        else:
            return bestMotifs
```

# How can this help us in the real world?
"In 2003, biologists found the dormancy survival regulator (DosR), a transcription factor that regulates many genes whose expression dramatically changes under hypoxic conditions. However, it remained unclear how DosR regulates these genes, and its transcription factor binding site remained unknown. In an attempt to resolve this puzzle, biologists performed a DNA array experiment and found 25 genes whose expression levels change significantly in hypoxic conditions. Given the upstream regions of these genes, each of which is 250 nucleotides long, we would like to discover the “hidden message” that DosR uses to control the expression of these genes."

Using our motif finding algorithms, we can attempt to solve this biological question.

# Cool

And thats what I think is incredibly fascinating about this stuff. Using the huge advances we have had in computational technology, we can try to answer real biological questions that could lead to discoveries and cures!




