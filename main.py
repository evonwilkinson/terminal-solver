from terminal_solver import TerminalSolver
from console_ui import ConsoleUI

if __name__ == "__main__":
    # Setup
    ui = ConsoleUI()
    ui.print_greeting()
    passwords_list = ui.get_words_from_user()
    ts = TerminalSolver(passwords_list)
    # Main solving loop
    while True:
        word, likeness = ui.get_word_likeness()
        ts.solve(word, likeness)
        if ts.unable_to_solve:
            print("Sorry, this terminal can not be hacked.")
            break
        if ts.solved:
            print("Solved! The password is", ts.correct_password)
            break
        print(ts.get_passwords())
