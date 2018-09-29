##  Classwork 2: Mad Props
####  Sam Chami, Jackson Myers, John Scott, and Ben Smith


###  Problem 1
1.  Create a KB by converting each of the above English sentences into a propositional logic one.

>  1.  M ⇔ (D ∨ P)
>  2.  R ⇒ (W ∨ S)
>  3.  R ⇔ D
>  4.  P ⇔ F
>  5.  (F ⇒ ¬W ∧ ¬S) ∧ (W ⇒ ¬F ∧ ¬S) ∧ (S ⇒ ¬F ∧ ¬W)
>  6.  M ∧ F

2.  Convert the KB into CNF, and enumerate each clause.

>  1.  KB1 = ¬M ∨ D ∨ P
>  2.  KB2 = ¬D ∨ M
>  3.  KB3 = ¬P ∨ M
>  4.  KB4 = ¬R ∨ W ∨ S
>  5.  KB5 = ¬R ∨ D
>  6.  KB6 = ¬D ∨ R
>  7.  KB7 = ¬P ∨ F
>  8.  KB8 = ¬F ∨ P
>  9.  KB9 = ¬F ∨ ¬S
>  10.  KB10 = ¬F ∨ ¬W
>  11.  KB11 = ¬S ∨ ¬W
>  12.  KB12 = M
>  13.  KB13 = F

3.  Using the above, we must settle the debate by showing that one of the following queries is true: (1) α = ¬D ∧ P (i.e., that it was an overheard paradox and NOT water damage that caused the uprising) or (2) β = ¬P ∧ D (vice versa).

>  14.  KB14 = D∨¬P
>  15.  [9,13] ⊨ KB15 = ¬S
>  16.  [10,13] ⊨ KB16 = ¬W
>  17.  [4,15] ⊨ KB17 = ¬R ∨ W
>  18.  [4,16] ⊨ KB18 = ¬R
>  19.  [6,18] ⊨ KB19 = ¬D
>  20.  [8,13] ⊨ KB20 = P
>  21.  [14,19] ⊨ KB21 = ¬P
>  22.  [20,21] ⊨ KB22 = ∅
>  23.  →←



###  Problem 2
1.  If an inference strategy only derives facts that are entailed by the KB, it is said to be __sound__. Sketch (briefly) a proof demonstrating that resolution is a sound inference strategy (hint: consider resolution's relationship to implication and Modus Ponens).

>  A sound inference strategy only derives facts that are entailed by the Knowledge Base. Resolution, a general form of Modus Ponens, uses two clauses that disagree on a literal from the KB to entail the query. Therefore Resolution is a sound inference strategy.

2.  If an inference strategy is guaranteed to (eventually) determine whether some sentence is entailed by the KB or not, it is called __complete__. Proof by resolution is known to be __refutation complete__, meaning that it is guaranteed to find a contradiction in the KB if one exists after adding the negation of the query to the KB. Apart from the KB being in CNF in order to apply resolution, what must be true about the KB to assume that resolution will be refutation complete (hint: consider what could happen with a poorly formed KB at the start)?

>  The KB must not be __inconsistent / contradictory__. In other words, a contradiction must not exist in the KB before any step of resolution is applied.
