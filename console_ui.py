class ConsoleUI:
    @staticmethod
    def get_words_from_user():
        passwords = []
        while True:
            entered_word = input("Enter a word: ")
            if not entered_word.isalpha():
                print("Only alpha characters are valid.")
                continue

            if entered_word == "done":
                confirmation = input("Are you sure you're finished? (y/n): ")
                confirmation = confirmation.lower()
                # TODO: Handle different comfirmation values (yes, YES, y, Y, etc.)
                if confirmation == "y":
                    print("Passwords received.")
                    break
                elif confirmation == "n":
                    continue

            if len(passwords) > 0 and len(entered_word) != len(passwords[0]):
                print("Word must have name number of letters as previous entries. Length: ", len(passwords[0]))

            passwords.append(entered_word)
        return passwords

    @staticmethod
    def get_word_likeness():
        print("Select a word on the terminal, then enter the word and the likeness below.")
        word = input("Enter the selected word: ")
        if not word.isalpha():
            print("Only alpha characters are valid.")
        likeness = input("Enter the likeness: ")
        if not likeness.isdigit():
            print("Only numbers are valid")
        return word, int(likeness)

    @staticmethod
    def print_greeting():
        print("---- Welcome to the Fallout 4 Terminal Solver ----")
        print("Please enter all the possible passwords shown on the terminal.")
        print("Type a word and press enter to add it to the solver. Type the word 'done' when you're finished.")
        print("")
