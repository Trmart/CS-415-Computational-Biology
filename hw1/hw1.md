# Project #1 - Genetic Algorithm

## CS414/515
## Spring 2023
## Due: Friday, February 24th

### The goal of this project is to perform two simple experiments using a genetic algorithm (GA).  Start with the GA we developed in class, but make any additions or modifications that are necessary for your experiment. Possible experiments include testing the effects of changing basic parameters of the GA:

    - Population size
    - Mutation rate
    - Selection pressure
    - Selection method

### More involved experiments could include:

    - Testing the effect of incorporating more accurate biological concepts: diploid genomes, more accurate versions of crossover, etc.
    - More complex fitness functions that are biologically more relevant.
    - Incorporating bottlenecks.
    - Incorporating merging or divergent populations.
    - Etc., etc., etc. 

Note that there are many ways to measure the effect of a parameter. Does it cause fitness to improve faster or slower? Does it cause the fitness to reach a maximum sooner or later? How does it effect population diversity? Etc.

If there is a way to relate your experiment to your graduate research, I strongly encourage you to do so, even if it means going a bit outside the box with regards to the project description.

You need to pick the details of the GA: population size, mutation rate, etc. If you are testing the impact of an adjustable parameter, then you should test a range of values. For example, if you are looking at mutation rate, you should test several different mutation rates, not just two.

# Project Write-up:

## Write a short research paper (typically 3-5 pages) describing the results of your project that includes the following sections:

    ### Abstract - a short summary of what you did and what the results were.
    ### Algorithm descriptions - clear, complete descriptions of your GA. Be careful to include all of the details someone would need to replicate your work. ### Examples of necessary details include (there are others):
        - How fitness is measured
        - Exactly how initial random individuals are generated
        - Mutation rates
        - Selection method
        - Etc.

## Basically every time you make a decision about how the algorithm works (what type of crossover it uses, how mutation is performed, etc.) you should make a note of it and include it in the algorithm description.

    - Results - include graphs and/or tables to make it easy to understand the results. Make sure that the graphs and table are clearly labeled.
    - Conclusions - based on your results draw some specific conclusions about how the algorithm performed.
