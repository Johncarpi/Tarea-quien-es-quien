
Práctica MIA - Quién es quién 
=============================

 * [Contenidos](#contenidos)
 * [El problema](#el-problema)
 * [Implementación](#implementación)
 * [Reglas del juego](#reglas-del-juego)
 * [Optimización vs Búsquedas](#1-optimización-vs-búsquedas)
 * [Entorno del agente](#2-entorno-del-agente)
 * [Algoritmo](#3-algoritmo)
 * [Estrutura del agente](#4-estrutura-del-agente)
 * [Programación lógica](#5-programación-lógica)
 * [Base de datos Prolog](#6-base-de-datos-prolog)
 * [Entrega](#entrega)
 * [Bibliografía](#bibliografía)

## Contenidos

Esta práctica involucra los contenidos del módulo de Modelos de Inteligencia Artificial tratados en las sesiones del curso:

 - [Algoritmos de búsqueda.](https://drive.google.com/drive/u/0/folders/1GSPdhrE0nXqVFnVk1hvhUUZ6R7cyjSqQ)
 - [Algoritmos de optimización.](https://drive.google.com/drive/u/0/folders/1z8J-1gUvP6i8WHhWh2FfobLOTxK1N_hH)
 - [Representación del conocimiento.](https://drive.google.com/drive/u/0/folders/1i3QhT8sDhuMnMTHek8lxCDWgWiMQVUGc)
 - [Lógica de primer orden.](https://drive.google.com/drive/u/0/folders/1DlTxaOVfo8HhoA-qQjrhvXuntBol3luL)
 - [Prolog.](https://github.com/dfleta/prolog-for-IA)

## El problema

Programa en Python y/o Prolog la lógica para resolver una partida del juego quién es quién. Puedes construir de manera completa el programa en Prolog. Si prefieres utilizar Python, al menos debes satisfacer el requisito de **construir una base de datos de hechos en Prolog** con los personajes y sus rasgos. 



## Contesta a las siguientes preguntas antes de desarrollar el programa agente.

### 1. Optimización vs Búsquedas

Este tipo de juego el 'quien es quien' puede ser considerado un problema de optimización ya que el programa
busca en todo momento encontrar a la persona que a sido seleccionada al azar en el menor tiempo posible a traves de una función
objetivo

### 2. Entorno del agente

Describe el entorno del agente en los términos tratados en la primera unidad didáctica y proyecto de este módulo.

Resume las características del entorno en una tabla con el formato:

Entorno de tareas | Completamente / parcialmente Observable| Agentes | Determinista / Estocástico | Episódico / Secuencial | Estático / Dinámico | Discreto / Continuo
:---: | :---: | :---: | :---: | :---: | :---: | :---: |
 Quien es quien | Parcialmente Observable | Monoagente | Determinista | Secuencial | Estático |  Discreto |

- Parcialmente observable: El jugador solo pueden ver su propio tablero, por lo que no conocen ni el tablero ni el personaje que tiene el rival el cual se tiene que adivinar descartando personajes de su propio tablero

- Monoagente: Se considera un agente Monoagente ya que un solo agente genera las preguntas y recoge las respuestas

- Determinista: las preguntas que se hacen solo tienen respuesta de si o no. No hay incertidumbre a la hora de responderlas.

- Secuencial: El hecho de realizar una pregunta puede cambiar y afectar decisiones futuras, ya que según la característica que se pregunte el tablero
podrá tener más o menos personajes activos

- Estático: El entorno nunca cambia hasta que se realiza una pregunta.

- Discreto: Existe un número finito tanto de características como de personajes por lo que tambien hay un número finito de preguntas

### 3. Algoritmo.

El algoritmo que utilizo consiste en buscar la característica que más se repite de los personajes y preguntar dicha característica para reducir considerablemente
el número de personajes en pie y acercarse al personaje objetivo.

### 4. Estrutura del agente

Nuestro propósito és diseñar el **programa agente** que implementa la **función agente** o la **función que mapea** las percepciones a las acciones. 

A partir del modelo general de agente inteligente de la figura:

[Esquema.odg](https://github.com/user-attachments/files/15775064/Esquema.odg)


**dibuja un modelo adecuado** al entorno de tareas y a un de los cuatro **tipos de programas agente**:

- Agentes reactivos simples.
- Agentes reactivos basados en modelos.
- Agentes basados en objetivos.
- Agentes basados en utilidad.

Cada clase de agente combina componentes particulares de un modo particular para generar las acciones. 

### 5. Programación lógica

El quien es quien se puede considerar un problema lógico debido a:

Posee una serie de reglas definidas que facilitan el uso de reglas lógicas para modelar su entrenamiento.

Las preguntas se formulan en términos de características y relaciones entre los personajes, estas se pueden representar fácilmente mediante predicados y relaciones en lógica.

Toda las características de los personajes pueden ser expresadas y tratadas con reglas lógicas.

Puedes aumentar las características de los personajes sin nigun tipo de problema.

### 6. Base de datos Prolog

Para este proyecto he utilizado una base de datos hecha en prolog la cual utilizo para extraer la información para mi programa.

La base de datos contiene a los personajes con sus características y contiene las funciones de prolog utilizadas para construir el tablero, contar las características
y sacar a los personajes segun sus características.

## Entrega

En un proyecto en tu github /gitlab con tu código y la documentación, esta última recogida en el `README` del proyecto y escrita en formato Markdown.

Para la instalación del proyecto, puedes utilizar el tutorial sobre distribución de código Python en el proyecto explicado en las sesiones del módulo:

[dependencias y pip-compile](https://github.com/dfleta/ollivanders?tab=readme-ov-file#dependencias)


## Bibliografía

Bratko, I. _Prolog, programming for Artificial Intelligence_. Addison-Wesley/Pearson, 2012.

Hurbans, Rishal. _grokking Artificial Intelligence Algorithms_. Manning Publications Co, 2020. 

Lutz, Mark. _Learning Python_. Sebastopol, Ca, O’reilly, 2018.

Martin, Robert C. _Clean Code a Handbook of Agile Software Craftmanship_. Upper Saddle River [Etc.] Prentice Hall, 2010.

Martin, Robert C. _Clean Architecture: A Craftsman’s Guide to Software Structure and Design_. Prentice Hall, 2018.

S. McConnel. _Code Complete: A Practical Handbook of Software Construction_, 2dn Edition. Microsoft Press, 2004.

Sharan, Kishori. _Beginning Java 8 Fundamentals: Language Syntax, Arrays, Data Types, Objects, and Regular Expressions_. Apress, 2014.

Russell, Peter. _ARTIFICIAL INTELLIGENCE : A Modern Approach_, Global Edition. S.L., Pearson Education Limited, 2021.

“Título de la fuente”, Título de recurso contenedor en cursiva, Fecha de publicación. Localización.

@dfleta. "Prolog for IA". _github_, 28 de febrero de 2024. https://github.com/dfleta/prolog-for-IA

@dfleta. "API REST con Flask y Mongo Atlas". _github_, 29 de marzo de 2022. https://github.com/dfleta/ollivanders
