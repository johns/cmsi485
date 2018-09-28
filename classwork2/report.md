##  Classwork 2: Mad Props
####  Jackson Myers, John Scott, and Ben Smith


###  Problem 1
1.  Create a KB by converting each of the above English sentences into a propositional logic one.

>  1.  M ⇔ (D ∨ P)
>  2.  R ⇒ (W ∨ S)
>  3.  R ⇔ D
>  4.  F ⇔ P
>  5.  F ⇒ ¬W ∧ ¬S
>  6.  W ⇒ ¬F ∧ ¬S
>  7.  S ⇒ ¬F ∧ ¬W
>  8.  F ∧ M

2.  Convert the KB into CNF, and enumerate each clause.

>  

3.  Using the above, we must settle the debate by showing that one of the following queries is true: (1) α = ¬D ∧ P (i.e., that it was an overheard paradox and NOT water damage that caused the uprising) or (2) β = ¬P ∧ D (vice versa).

>  


###  Problem 2
1.  If an inference strategy only derives facts that are entailed by the KB, it is said to be __sound__. Sketch (briefly) a proof demonstrating that resolution is a sound inference strategy (hint: consider resolution's relationship to implication and Modus Ponens).

>  A sound inference strategy only derives facts that are entailed by the Knowledge Base. Resolution, a general form of Modus Ponens, uses two clauses that disagree on a literal from the KB to entail the query. Therefore Resolution is a sound inference strategy.

2.  If an inference strategy is guaranteed to (eventually) determine whether some sentence is entailed by the KB or not, it is called __complete__. Proof by resolution is known to be __refutation complete__, meaning that it is guaranteed to find a contradiction in the KB if one exists after adding the negation of the query to the KB. Apart from the KB being in CNF in order to apply resolution, what must be true about the KB to assume that resolution will be refutation complete (hint: consider what could happen with a poorly formed KB at the start)?

> In order for the resolution to be refutation complete, a KB must have a proposition p which the union KB U (negated)p is inconsistent.
