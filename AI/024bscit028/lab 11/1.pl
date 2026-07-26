/* ---------- Facts ---------- */

male(ram).
male(hari).

female(sita).
female(gita).

parent(ram, hari).
parent(sita, hari).
parent(gita, sita).

/* ---------- Rules ---------- */

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

/* ---------- List Operations ---------- */

% Membership
my_member(X, [X|_]).
my_member(X, [_|T]) :-
    my_member(X, T).

% Length
my_length([], 0).
my_length([_|T], N) :-
    my_length(T, N1),
    N is N1 + 1.

% Concatenation
my_concat([], L, L).
my_concat([H|T], L, [H|R]) :-
    my_concat(T, L, R).

% Insert at beginning
insert(X, L, [X|L]).

% Delete an element
delete(_, [], []).
delete(X, [X|T], T).
delete(X, [H|T], [H|R]) :-
    delete(X, T, R).

% Append element at end
append_end([], X, [X]).
append_end([H|T], X, [H|R]) :-
    append_end(T, X, R).