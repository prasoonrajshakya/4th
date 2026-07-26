/* ---------- Facts ---------- */

studied(radha).
studied(rakesh).
studied(anish).

not_studied(rekha).
not_studied(bibek).


/* ---------- Rules ---------- */

pass(X) :-
    studied(X).

happy(X) :-
    pass(X).