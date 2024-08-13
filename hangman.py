import tkinter as tk
import random


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = self.get_word()
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.tries = 6

        self.create_widgets()

    def get_word(self):
        words = ["python", "hangman", "challenge", "programming", "openai", "artificial", "intelligence"]
        return random.choice(words).upper()

    def create_widgets(self):
        self.hangman_label = tk.Label(self.root, text=self.display_hangman(), font=('Helvetica', 30))
        self.hangman_label.pack(pady=10)



        self.label = tk.Label(self.root, text=" ".join("_" * len(self.word)), font=('Helvetica', 18))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=('Helvetica', 18))
        self.entry.pack(pady=20)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()


    def check_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                self.label.config(text=f"You already guessed the letter {guess}")
            elif guess in self.word_letters:
                self.guessed_letters.add(guess)
                self.word_letters.remove(guess)
            else:
                self.tries -= 1
                self.guessed_letters.add(guess)

            self.update_display()

        if "_" not in self.label['text']:
            self.label.config(text=f"Congratulations! The word was {self.word}")
            self.submit_button.config(state='disabled')
        elif self.tries == 0:
            self.label.config(text=f"Sorry, you ran out of tries. The word was {self.word}")
            self.submit_button.config(state='disabled')

    def update_display(self):
        word_display = [letter if letter in self.guessed_letters else '_' for letter in self.word]
        self.label.config(text=" ".join(word_display))
        self.hangman_label.config(text=self.display_hangman())

    def display_hangman(self):
        stages = [
            """
               -----
               |   |
               |   O
               |  /|\\
               |  / \\
               -
            """,
            """
               -----
               |   |
               |   O
               |  /|\\
               |  / 
               -
            """,
            """
               -----
               |   |
               |   O
               |  /|\\
               |  
               -
            """,
            """
               -----
               |   |
               |   O
               |  /|
               |  
               -
            """,
            """
               -----
               |   |
               |   O
               |   |
               |  
               -
            """,
            """
               -----
               |   |
               |   O
               |  
               |  
               -
            """,
            """
               -----
               |   |
               |   
               |  
               |  
               -
            """
        ]
        return stages[self.tries]


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()