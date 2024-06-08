
import random
import pyswip
from pyswip import Prolog


class WhoIsWhoGame:
    # Consultamos la base de datos prolog y seleccionamos um personaje al azar
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult(r'C:\Users\34658\Desktop\Ejercicios\Tarea-quien-es-quien\quienesquien-main\src\prueba.pl')  
        self.tablero = [str(char) for char in list(self.prolog.query("levantar_tablero(Tablero)"))[0]['Tablero']]
        self.characteristics = ["sombrero", "gafas", "bigote", "barba", "pelo", "altura"]
        self.target_character = random.choice(self.tablero)

    # La función para prefuntar una característica al juego
    def ask_question(self, characteristic, value=None):
        if value:
            query = f"{characteristic}({self.target_character}, {value})"
        else:
            query = f"tiene({self.target_character}, {characteristic})"
        result = bool(list(self.prolog.query(query)))
        return result

    def select_best_question(self):
        best_question = None
        best_split = len(self.tablero)
        for characteristic in self.characteristics:
            for value in [True, False]:
                formatted_tablero = "[" + ",".join(f"'{char}'" for char in self.tablero) + "]"
                query = f"bajar({characteristic}, {formatted_tablero}, S)" if value else f"bajar_not({characteristic}, {formatted_tablero}, S)"
                result = list(self.prolog.query(query))
                if result:
                    split = len(result[0]['S'])
                    if split < best_split:
                        best_split = split
                        best_question = (characteristic, value)
        return best_question

    # Función para actualizar el tablero
    def update_board(self, characteristic, answer, value=None):
    
        formatted_tablero = "[" + ",".join(f"'{char}'" for char in self.tablero) + "]"
        if value:
            if answer:
                query = f"bajar({value}, {formatted_tablero}, S)"
            else:
                query = f"bajar_not({value}, {formatted_tablero}, S)"
        else:
            if answer:
                query = f"bajar({characteristic}, {formatted_tablero}, S)"
            else:
                query = f"bajar_not({characteristic}, {formatted_tablero}, S)"
        self.tablero = [str(char) for char in list(self.prolog.query(query))[0]['S']]

    # El juego
    def play(self):
        print("Empieza el juego")
        while len(self.tablero) > 1:
            print(f"Personajes en pie: {', '.join(self.tablero)}")
            best_question = self.select_best_question()
            if best_question:
                characteristic, value = best_question
                answer = self.ask_question(characteristic, value)
                print(f"El personaje tiene {characteristic} {value if value else ''}? {'Sí' if answer else 'No'}")
                self.update_board(characteristic, answer, value)
            else:
                print("No se puede encontrar una pregunta óptima, continuando con la estrategia estándar.")
                question = random.choice(self.characteristics)
                answer = self.ask_question(question)
                print(f"El personaje tiene {question}? {'Sí' if answer else 'No'}")
                self.update_board(question, answer)

        print(f"El personaje es: {self.tablero[0]}")
        if self.tablero[0] == self.target_character:
            print("¡Felicidades! Has acertado el personaje correcto.")
        else:
            print("¡Vaya! Algo salió mal.")
            
if __name__ == "__main__":
    game = WhoIsWhoGame()
    game.play()
