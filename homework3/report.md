##  Homework 3: Having a Bayes Ball
####  Sam Chami and John Scott


###  I. Bayesian Network Modeling

Include the following in your report:

1.  Capture some output for your report by taking a picture of the network structure (can drag the nodes around to make it prettier).
>  ![Photo](DAG.png)

2.  Look up the PC Structure Learning algorithm and write a short summary on how it orients edges in the network structure.
>  The PC Structure Learning Algorithm uses statistical tests to determine conditional independents between variables. The algorithm starts by checking for independence among each variables. Wherevers a variable is found to be dependent of another, an undirected link is formed between the two nodes. The algorithm then finds all possible "colliders", which are variables and independence statements that cross and direct a link. (E.g.: In the above graph, F -> S <- G was determined via a collider). After this, links are formed and put in place for all nodes of the graph. The algorithm then calls for any undirected links (as there is no guarantee that every direction will be picked), and picks a random direction. This is meant to complete the graph and causes no harm because the directions can be manually switched because of human intuition.

3.  Explain, using the theory behind this algorithm, why it was able to orient some edges but not others. Reference the graph you found above.
>  TODO


###  II. Decision Network Modeling

In a small paragraph, argue for whether or not you believe this practice should be considered ethical, especially if each individual's characteristics were collected via social media. Compare this practice to targeted political advertising wherein ads are curated based on perceived in-group.
>  TODO
