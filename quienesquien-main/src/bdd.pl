% Definición de los personajes y sus características
personaje(max, [sombrero, gafas, bigote]).
personaje(susan, [barba, pelo, altura]).
personaje(tom, [sombrero, gafas, pelo]).
personaje(sam, [bigote, barba, altura]).
% Añade más personajes según sea necesario...

% Levantar el tablero inicial
levantar_tablero(Tablero) :-
    findall(Personaje, personaje(Personaje, _), Tablero).

% Predicados para verificar características
tiene(Personaje, Caracteristica) :-
    personaje(Personaje, Caracteristicas),
    member(Caracteristica, Caracteristicas).

% Predicados para bajar personajes según características
bajar(Caracteristica, Tablero, S) :-
    findall(Personaje, (member(Personaje, Tablero), tiene(Personaje, Caracteristica)), S).

bajar_not(Caracteristica, Tablero, S) :-
    findall(Personaje, (member(Personaje, Tablero), \+ tiene(Personaje, Caracteristica)), S).

% Contar personajes con una característica
count_characters_with(Caracteristica, Count) :-
    findall(Personaje, tiene(Personaje, Caracteristica), List),
    length(List, Count).

% Contar personajes sin una característica
count_characters_without(Caracteristica, Count) :-
    findall(Personaje, (personaje(Personaje, _), \+ tiene(Personaje, Caracteristica)), List),
    length(List, Count).

