% Facts
parent(james_1, charles_1).
parent(james_1, elizabeth).

parent(charles_1, catherine).
parent(charles_1, charles_2).
parent(charles_1, james_2).

parent(elizabeth, sophia).
parent(sophia, george_1).

male(james_1).
male(charles_1).
male(charles_2).
male(james_2).
male(george_1).

female(elizabeth).
female(catherine).
female(sophia).

% Rules
child(Child, Parent) :-
    parent(Parent, Child).

sibling_of(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

sister_of(X, Y) :-
    female(X),
    sibling_of(X, Y).

brother_of(X, Y) :-
    male(X),
    sibling_of(X, Y).