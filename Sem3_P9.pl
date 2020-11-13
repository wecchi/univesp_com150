% Fatos
responsavel(a,b).
responsavel(d,c).
responsavel(c,e).
responsavel(d,g).
responsavel(f,h).
responsavel(a,i).

% #Regras
gerencia(X,Y) :-
    responsavel(X,Y).
gerencia(X,Y) :-
    responsavel(X,Z),
    gerencia(Z,Y).


