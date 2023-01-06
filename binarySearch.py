def binary_search(hidden_word, guess):
    # Set the initial values for the search range
    low = 0
    high = len(hidden_word) - 1

    # Loop until the search range is exhausted
    while low <= high:
        mid = (low + high) // 2
        if hidden_word[mid] < guess:
            low = mid + 1
        elif hidden_word[mid] > guess:
            high = mid - 1
        else:
            # The guess has been found
            return True

    # The guess was not found
    return False


# Test the function
hidden_word = ["apple"]

mess = '''==Guessing Game==
You have 3 guesses only to win this game! Gooluck mate!'''
print(mess)

# Allow the user to make at most 3 guesses
for i in range(3):
    # Get a guess from the user
    guess = input("\nEnter your guess: ")
    if binary_search(hidden_word, guess):
        print("\nYou guessed the hidden word! You win!")
        break
    else:
        if i+2 <= 3:
            print("\nThat is not the hidden word. Try again.")
            pass
else:
    print("\nYou did not guess the hidden word. You lose Mate!")
