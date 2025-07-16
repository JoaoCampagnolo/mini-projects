import random

def choose_word():
    # Example list of words. Replace or extend this list as per your requirement.
    words = ["heart", "flirt", "crush", "charm", "adore"]
    return random.choice(words)

def get_guess():
    guess = input("Enter your guess (5 letters): ").lower()
    while len(guess) != 5 or not guess.isalpha():
        guess = input("Invalid input. Please enter a 5-letter word: ").lower()
    return guess

def compare_words(word, guess):
    result = ""
    for i in range(5):
        if guess[i] == word[i]:
            result += "🟩"
        elif guess[i] in word:
            result += "🟨"
        else:
            result += "⬛"
    return result

def play_wordle():
    word = choose_word()
    attempts = 6

    print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")

    for attempt in range(attempts):
        guess = get_guess()
        result = compare_words(word, guess)
        print(" ".join(guess.upper()))
        print(result)
        if guess == word:
            print("Congratulations! You've guessed the word correctly!")
            print("""
            🎉 Congratulations, Em! 🎉

            You've reached the end of our anniversary scavenger hunt, and I couldn't be prouder of you. This past year with you has been the most incredible journey of my life, and every day I feel so lucky to have you by my side. You are the best thing that has ever happened to me, and I look forward to all the adventures that lie ahead for us. Here's to many more years of love, laughter, and happiness together.

            With all my love,
            João
            """)
            print("PS: Check the kitchen cupboard for a final gift!")

            break
    else:
        print(f"Sorry, you've run out of attempts. The word was: {word}")

if __name__ == "__main__":
    print("\n🔤 With letters scattered, hidden in plain sight,")
    print("Wordle calls, to challenge your might.")
    print("Five tries you have, to get it right,")
    print("Unveil the word, bring it to light. 🌟\n")
    play_wordle()


































    