import random

word_list = ["purple", "banana", "rocket", "monkey", "waffle", "silver", "guitar"]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def analyze_letter_usage(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    usage = {letter: 0 for letter in letters}
    for letter in word:
        if letter in letters:
            usage[letter] += 1
    return usage

def print_session_summary(attempts, word_to_guess):
    print("\nSession Summary:")
    print(f"Attempts remaining: {attempts}")
    print(f"The word was: {word_to_guess}")

def main():
    print("Welcome to the Word Guessing Game!")

    while True:  # Outer loop to play the game again
        word_to_guess = choose_random_word(word_list)
        guessed_letters = []
        attempts = 6

        while True:  # Inner loop for a single game
            print("\nMenu:")
            print("1. Analyze Letter Usage")
            print("2. Play Game")
            print("3. Print Session Summary")
            print("X. Exit Program")
            menu_choice = input("Enter your choice: ").lower()

            if menu_choice == "1":
                letter_usage = analyze_letter_usage(word_to_guess)
                for letter, count in letter_usage.items():
                    print(f"{letter}: {count} times")
            elif menu_choice == "2":
                while attempts > 0:
                    current_display = display_word(word_to_guess, guessed_letters)
                    print("\nWord to guess:", current_display)
                    guess = input("Guess a letter: ").lower()

                    if len(guess) != 1 or not guess.isalpha():
                        print("Please enter a single letter.")
                    elif guess in guessed_letters:
                        print("You already guessed that letter.")
                    else:
                        guessed_letters.append(guess)

                        if guess in word_to_guess:
                            print("Good guess!")
                            for i, letter in enumerate(word_to_guess):
                                if letter == guess:
                                    current_display = current_display[:i] + letter + current_display[i + 1:]
                            if current_display == word_to_guess:
                                print("Congratulations! You've guessed the word:", word_to_guess)
                                break
                        else:
                            print("Wrong guess.")
                            attempts -= 1
                            print(f"Attempts left: {attempts}")

                    if attempts == 0:
                        print("Sorry, you're out of attempts. The word was:", word_to_guess)
            elif menu_choice == "3":
                print_session_summary(attempts, word_to_guess)
            elif menu_choice == "x":
                print("Exiting the program.")
                return
            else:
                print("Invalid option. Please select a valid menu option.")

            play_again = input("Do you want to play again? (yes or no): ").lower()
            if play_again != "yes":
                print("Exiting the game.")
                break

if __name__ == "__main__":
    main()