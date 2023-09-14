#guess me
guess_word = "source"
guess = ""
total_guesses = 3
guess_count = 0
out_of_guesses = False

while guess != guess_word and not out_of_guesses:
    if guess_count < total_guesses:
        guess = input("guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, you lose")
else:
    print("you won!")