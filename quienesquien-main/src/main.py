import random
from pyswip import Prolog

class WhoIsWhoGame:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult('/media/TEIS/a23juancm/Python/quienesquien-main/src/quienesquien.pl')
        self.tablero = list(self.prolog.query("levantar_tablero(Tablero)"))[0]['Tablero']
        self.characteristics = ["sombrero", "gafas", "bigote", "barba"]
        self.target_character = random.choice(self.tablero)

    def ask_question(self, characteristic):
        query = f"tiene({self.target_character}, {characteristic})"
        result = bool(list(self.prolog.query(query)))
        return result

    def update_board(self, characteristic, answer):
        # Convert Prolog atoms to strings
        formatted_tablero = "[" + ",".join(f"'{char}'" for char in self.tablero) + "]"
        if answer:
            query = f"bajar({characteristic}, {formatted_tablero}, S)"
        else:
            query = f"bajar_not({characteristic}, {formatted_tablero}, S)"
        self.tablero = list(self.prolog.query(query))[0]['S']

    def play(self):
        print("Welcome to Who is Who!")
        while len(self.tablero) > 1:
            print(f"Current characters: {self._format_characters(self.tablero)}")
            resolve = input('Do you want to guess the person [1] or continue [0]?: ')
            if resolve not in ["0", "1"]:
                print("Invalid input! Please enter 0 to continue or 1 to guess.")
                continue

            if resolve == "0":
                question = input(f"Ask a question about a characteristic {self.characteristics}: ")
                if question not in self.characteristics:
                    print("Invalid characteristic! Please choose from the available list.")
                    continue

                answer = self.ask_question(question)
                print(f"Does the character have {question}? {'Yes' if answer else 'No'}")
                self.update_board(question, answer)
            else:
                guess = input('Please input the name of the character: ')
                if guess == self.target_character:
                    print("Congratulations! You guessed it right.")
                else:
                    print(f"Oops! That's not correct. The character is: {self._format_character(self.target_character)}")
                return

        print(f"The character is: {self._format_character(self.tablero[0])}")
        if len(self.tablero) == 1 and self.tablero[0] == self.target_character:
            print("Congratulations! You narrowed it down to the right character.")
        else:
            print("Oops! Something went wrong.")

    def _format_characters(self, characters):
        return [self._format_character(char) for char in characters]

    def _format_character(self, character):
        return str(character)

if __name__ == "__main__":
    game = WhoIsWhoGame()
    game.play()
