class TerminalSolver:
    def __init__(self, words):
        # List to store possible passwords
        self.words = words
        self.solved = False
        self.unable_to_solve = False
        self.correct_password = ""

    def solve(self, word, likeness):
        passwords_to_remove = []
        correct_letters = 0
        # Remove the entered word as it cannot be the correct password
        self.words.remove(word)

        # The entered word doesn't match the correct password so return
        if likeness == 0:
            return

        for possible_password in self.words:
            for i in range(len(possible_password)):
                # Count the number of letters that match in both value and position
                if possible_password[i] == word[i]:
                    correct_letters += 1
            if correct_letters != likeness:
                # If the word being compared doesn't match the likeness, it can't be a possible correct password
                passwords_to_remove.append(possible_password)
            correct_letters = 0

        # If a password is removed from the list of possible passwords during the letter comparison loop,
        # the next word to be compared in the list will be skipped over as the list is re-ordered.
        # My solution is to add the word to a temporary list and then remove the incorrect words after the
        # comparison loop.
        for password in passwords_to_remove:
            self.words.remove(password)

        # No more words left in the password list means it can't be solved, most likely due to a mistake in
        # the entered words
        if len(self.words) == 0:
            self.unable_to_solve = True

        # Last word in the last must be the correct password
        if len(self.words) == 1:
            self.solved = True
            self.correct_password = self.words[0]

    def get_passwords(self):
        return self.words
