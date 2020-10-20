% Fatores
come(urso, peixe).
come(urso, raposa).
come(urso, veado).
come(veado, grama).
come(peixe, peixinho).
come(peixinho, alga).
come(guaxinim, peixe).
come(urso, guaxinin).
come(raposa, coelho).
come(coelho, grama).
come(coelho, flores).
come(lince, veado).

animal(urso).
animal(peixe).
animal(peixinho).
animal(raposa).
animal(guaxinim).
animal(coelho).
animal(lince).
animal(veado).

planta(grama).
planta(flores).
planta(alga).

% Regras
presa(X) :-
    come(_, X),
    animal(X).

predador(X) :-
    come(X, Y),
    animal(Y).

herbivoro(X) :-
    come(X,Y),
    planta(Y).

cadeiaalimentar(X, Y) :-
    come(X, Y).
cadeiaalimentar(X, Y) :-
    come(X, Z),
    cadeiaalimentar(Z,Y).

