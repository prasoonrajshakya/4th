/* ---------- Facts ---------- */
likes(john, ai).
likes(john, cs).
likes(sara, ai).

/* ---------- Rule ---------- */

likes(jack, X) :-
    likes(sara, X).

dislikes(sara, cs).