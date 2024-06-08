% quienesquien.pl

% Characters
personaje(max).
personaje(susan).
personaje(tom).
personaje(sam).
personaje(anne).
personaje(robert).
personaje(anita).
personaje(bill).
personaje(bernard).
personaje(alfred).
personaje(frans).
personaje(george).
personaje(david).
personaje(paul).
personaje(joe).
personaje(philip).
personaje(peter).
personaje(alex).
personaje(eric).
personaje(richard).
personaje(charles).
personaje(claire).
personaje(maria).
personaje(herman).

% Characteristics
tiene(max, sombrero).
tiene(susan, gafas).
tiene(tom, bigote).
tiene(sam, barba).
tiene(anne, sombrero).
tiene(robert, gafas).
tiene(anita, bigote).
tiene(bill, barba).
tiene(bernard, sombrero).
tiene(alfred, gafas).
tiene(frans, bigote).
tiene(george, barba).
tiene(david, sombrero).
tiene(paul, gafas).
tiene(joe, bigote).
tiene(philip, barba).
tiene(peter, sombrero).
tiene(alex, gafas).
tiene(eric, bigote).
tiene(richard, barba).
tiene(charles, sombrero).
tiene(claire, gafas).
tiene(maria, bigote).
tiene(herman, barba).

% New Characteristics
pelo(max, rubio).
pelo(susan, castaño).
pelo(tom, negro).
pelo(sam, castaño).
pelo(anne, pelirrojo).
pelo(robert, rubio).
pelo(anita, negro).
pelo(bill, castaño).
pelo(bernard, pelirrojo).
pelo(alfred, rubio).
pelo(frans, castaño).
pelo(george, negro).
pelo(david, pelirrojo).
pelo(paul, castaño).
pelo(joe, rubio).
pelo(philip, negro).
pelo(peter, pelirrojo).
pelo(alex, castaño).
pelo(eric, rubio).
pelo(richard, castaño).
pelo(charles, pelirrojo).
pelo(claire, castaño).
pelo(maria, negro).
pelo(herman, rubio).

altura(max, alto).
altura(susan, baja).
altura(tom, medio).
altura(sam, alto).
altura(anne, baja).
altura(robert, medio).
altura(anita, baja).
altura(bill, alto).
altura(bernard, medio).
altura(alfred, alto).
altura(frans, medio).
altura(george, bajo).
altura(david, alto).
altura(paul, medio).
altura(joe, alto).
altura(philip, bajo).
altura(peter, medio).
altura(alex, alto).
altura(eric, bajo).
altura(richard, alto).
altura(charles, medio).
altura(claire, baja).
altura(maria, media).
altura(herman, bajo).

% Predicate to list all characters
levantar_tablero(Tablero) :- findall(X, personaje(X), Tablero).

% Predicate to check if a character has a certain characteristic
caracteristicas(Personaje, Caracteristicas) :- findall(C, tiene(Personaje, C), Caracteristicas).

% Predicate to eliminate characters based on a characteristic they don't have
bajar(Caracteristica, [H|T], S) :-
    ( tiene(H, Caracteristica) ; pelo(H, Caracteristica) ; altura(H, Caracteristica) ),
    bajar(Caracteristica, T, ST),
    append([H], ST, S).
bajar(Caracteristica, [_|T], S) :- bajar(Caracteristica, T, S).
bajar(_, [], []).

% Predicate to eliminate characters based on a characteristic they have
bajar_not(Caracteristica, [H|T], S) :-
    not(tiene(H, Caracteristica)),
    not(pelo(H, Caracteristica)),
    not(altura(H, Caracteristica)),
    bajar_not(Caracteristica, T, ST),
    append([H], ST, S).
bajar_not(Caracteristica, [_|T], S) :- bajar_not(Caracteristica, T, S).
bajar_not(_, [], []).

% Predicate to update the list of remaining characters
f_sucesora(Caracteristica, [H|T], Tablero, S) :- 
    tiene(H, Caracteristica),
    bajar(H, Tablero, ST),
    f_sucesora(Caracteristica, T, ST, S).
f_sucesora(Caracteristica, [_|T], Tablero, S) :- f_sucesora(Caracteristica, T, Tablero, S).
f_sucesora(_, [], Tablero, Tablero).

% Predicate to add unique characteristics to a list
add_not([H|T], List, L) :- member(H, List), add_not(T, List, L).
add_not([H|T], List, [H|L]) :- not(member(H, List)), add_not(T, List, L).
add_not([], L, L).

% Predicate to test if a character is the goal character
test([X], X).
test([_|T], X) :- test(T, X).
