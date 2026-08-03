% directed graph
edge(s, a).
edge(s, b).
edge(a, e).
edge(a, c).
edge(b, e).
edge(e, g).

% path
path(Start, End):-
    travel(Start, End, [Start]).

travel(X, Y, _):-
    edge(X, Y).

travel(X, Y, Visited):-
    edge(X, Z),
    \+ member(Z, Visited),
    travel(Z, Y, [Z|Visited]).