import random
from pyswip import Prolog
import math


class WhoIsWhoGame:
    # Conectamos con prolog
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult(
            "src/bdd.pl"
        )
        # Realizamos una consulta a la base de datos de prolog para levantar el tablero
        self.tablero = [
            str(char)
            for char in list(self.prolog.query("levantar_tablero(Tablero)"))[0][
                "Tablero"
            ]
        ]

        # Definimos las características de los personajes del tablero
        self.characteristics = [
            "sombrero",
            "gafas",
            "bigote",
            "barba",
            "pelo",
            "altura",
        ]

        # Ahora escogeremos el personaje a adivinar en el tablero, este se escogera a lo ramdom.
        self.target_character = random.choice(self.tablero)
        self.last_question = None

    # Esta es la función donde preguntaremos por la característica 
    def ask_question(self, characteristic):
        #realizamos la consulta
        query = f"tiene({self.target_character}, {characteristic})"
        result = bool(list(self.prolog.query(query)))
        return result

    # Esta es la función donde buscaremos la mejor pregunta que se puede hacer para intentar reducir en la mayor medida a los personajes.
    def select_best_question(self):
        best_question = None
        best_entropy = float("inf")

        # Esta variable se utiliza para coger el valor de la última pregunta realizada ypara evitar que esta se repita
        last_index = (
            self.characteristics.index(self.last_question) if self.last_question else -1
        )

        # Se incrementa el índice para seleccionar la siguiente característica
        next_index = (last_index + 1) % len(self.characteristics)

        # Seleccionamos la siguiente característica
        characteristic = self.characteristics[next_index]

        count_with_query = f"count_characters_with({characteristic}, Count)"
        count_without_query = f"count_characters_without({characteristic}, Count)"
        count_with = list(self.prolog.query(count_with_query))[0]["Count"]
        count_without = list(self.prolog.query(count_without_query))[0]["Count"]

        p_with = count_with / len(self.tablero)
        p_without = count_without / len(self.tablero)

        entropy = -p_with * math.log2(p_with) if p_with > 0 else 0
        entropy -= p_without * math.log2(p_without) if p_without > 0 else 0

        if entropy < best_entropy and count_with > 0 and count_without > 0:
            best_entropy = entropy
            best_question = characteristic

        self.last_question = best_question
        return best_question

    # Función para actualizar el tablero
    def update_board(self, characteristic, answer):

        # Formateamos el tablero ya que prolog me da un error con el tipo de formato de las variables de los personajes
        formatted_tablero = "[" + ",".join(f"'{char}'" for char in self.tablero) + "]"
        query = (
            f"bajar({characteristic}, {formatted_tablero}, S)"
            if answer
            else f"bajar_not({characteristic}, {formatted_tablero}, S)"
        )
        # Actualizamos el tablero
        self.tablero = [str(char) for char in list(self.prolog.query(query))[0]["S"]]

    # El juego en si 
    def play(self):
        print("Empieza el juego")
        # Mientras No esxista solo un personaje en el tablero el juego sigue continuando
        while len(self.tablero) > 1:
            # Mostramos los personajes que siguen en pie
            print(f"Personajes en pie: {', '.join(self.tablero)}")
            # Obtenemos la pregunta
            best_question = self.select_best_question()
            if best_question:
                answer = self.ask_question(best_question)
                # Mostramos si el personaje tiene esa carcterítica.
                print(f"El personaje tiene {best_question}? {'Sí' if answer else 'No'}")
                # Actualizamos el tablero
                self.update_board(best_question, answer)
            else:
                print(
                    "No se puede encontrar una pregunta óptima, continuando con la estrategia estándar."
                )
                question = random.choice(
                    [
                        char
                        for char in self.characteristics
                        if char != self.last_question
                    ]
                )
                answer = self.ask_question(question)
                print(f"El personaje tiene {question}? {'Sí' if answer else 'No'}")
                self.update_board(question, answer)
        # Mostramos el personaje el cual era el objetivo
        print(f"El personaje es: {self.tablero[0]}")
        if self.tablero[0] == self.target_character:
            print("¡Felicidades! Has acertado el personaje correcto.")
        else:
            print("¡Vaya! Algo salió mal.")


if __name__ == "__main__":
    game = WhoIsWhoGame()
    game.play()
