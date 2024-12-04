from breezypythongui import EasyFrame


class GuessingGame(EasyFrame):
    def __init__(self):
        """Initialize the GUI and game logic."""
        super().__init__(title="Guess the Number Game")

        # Initial state
        self.low = 1
        self.high = 100
        self.guess = 50

        # Label to display the computer's guess
        self.guessLabel = self.addLabel(
            text=f"My guess is {self.guess}.", row=0, column=0, columnspan=3, sticky="NSEW")

        # Feedback buttons
        self.tooSmallButton = self.addButton(
            text="Too Small", row=1, column=0, command=self.tooSmall)
        self.tooLargeButton = self.addButton(
            text="Too Large", row=1, column=1, command=self.tooLarge)
        self.correctButton = self.addButton(
            text="Correct", row=1, column=2, command=self.correct)

        # New game button
        self.newGameButton = self.addButton(
            text="New Game", row=2, column=1, command=self.newGame)
        self.newGameButton["state"] = "disabled"  # Initially disabled

    def tooSmall(self):
        """Handles 'Too Small' button."""
        self.low = self.guess + 1
        self.updateGuess()

    def tooLarge(self):
        """Handles 'Too Large' button."""
        self.high = self.guess - 1
        self.updateGuess()

    def correct(self):
        """Handles 'Correct' button."""
        self.guessLabel["text"] = f"I guessed it! The number is {self.guess}."
        self.disableButtons()

    def updateGuess(self):
        """Updates the computer's guess and label."""
        if self.low > self.high:
            self.guessLabel["text"] = "Error! The range is invalid."
            self.disableButtons()
        else:
            self.guess = (self.low + self.high) // 2
            self.guessLabel["text"] = f"My guess is {self.guess}."

    def disableButtons(self):
        """Disables feedback buttons."""
        for button in [self.tooSmallButton, self.tooLargeButton, self.correctButton]:
            button["state"] = "disabled"
        self.newGameButton["state"] = "normal"

    def newGame(self):
        """Resets the game."""
        self.low = 1
        self.high = 100
        self.guess = 50
        self.guessLabel["text"] = f"My guess is {self.guess}."
        self.enableButtons()

    def enableButtons(self):
        """Enables feedback buttons."""
        for button in [self.tooSmallButton, self.tooLargeButton, self.correctButton]:
            button["state"] = "normal"
        self.newGameButton["state"] = "disabled"


# Run the program
if __name__ == "__main__":
    GuessingGame().mainloop()
