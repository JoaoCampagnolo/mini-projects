import random

class LyricsGame():
    def __init__(self):
        pass
        # Extended list of song lyrics with missing words, answers, and their respective song and artist
        self.lyrics = [
            ("When the rain is blowing in your face, and the whole world is on your case, I could offer you a warm _____", "embrace", "Make You Feel My Love - Adele"),
            ("You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us, and the world will live as _____", "one", "Imagine - John Lennon"),
            ("I've paid my dues, time after time. I've done my sentence but committed no _____", "crime", "We Are the Champions - Queen"),
            ("And I think to myself, what a wonderful _____", "world", "What a Wonderful World - Louis Armstrong"),
            ("Clap along if you feel like a room without a _____", "roof", "Happy - Pharrell Williams"),
            # Placeholder lyrics for the requested songs
            ("Vi går ned til vandet, hvor alt er så _____", "lækker", "Lækker - Nik & Jay"),
            ("Og vi løber gennem byen, ingen kan fange os, vi er _____", "ung", "Ung Kniv - The Minds of 99"),
            ("Yo, I'll tell you what I want, what I really really want, So tell me what you want, what you really really _____", "want", "Wannabe - Spice Girls"),
            ("Whenever blue teardrops are falling and my emotional stability is leaving me, there is something I can do, I can get on the telephone and call you up baby, and _____ you'll be there", "hope", "Sexual Healing - Marvin Gaye"),
            ("You belong with me, you belong with me, walking the streets with you and your worn-out jeans, I can't help thinking this is how it _____ to be", "ought", "You Belong With Me - Taylor Swift"),
            ("I'm a, a diva, hey, I'm a, I'm a _____", "diva", "Diva - Beyonce"),
            ("Oh baby, baby, how was I supposed to know that something wasn't _____", "right", "...Baby One More Time - Britney Spears"),
            ("No more watchin' of the _____, heart rate slows", "clock", "Casio - Jungle")
        ]

    # The game
    def guess_the_lyrics(self):
        # Randomly select a lyric
        lyric, correct_word, song_artist = random.choice(self.lyrics)
        
        print("\nGuess the missing word in the lyric and the song name with artist:")
        print(lyric)
        
        attempts = 3
        while attempts > 0:
            user_guess_word = input("Your guess for the missing word: ").strip().lower()
            user_guess_song = input("Your guess for the song and artist (e.g., Song - Artist): ").strip().lower()
            
            if user_guess_word == correct_word.lower() and user_guess_song.lower() == song_artist.lower():
                print("Correct! You've guessed both the word and the song correctly.")
                return True
            else:
                attempts -= 1
                print(f"Oops! That's not quite right. You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
        
        if attempts == 0:
            print(f"Sorry, you're out of attempts. The correct word was '{correct_word}', and the song was '{song_artist}'.")
            return False


if __name__ == "__main__":
    print("🎵 In a world where lyrics and melody embrace,")
    print("Your memory and wit now take their place.")
    print("Guess the words left unsung, in the air,")
    print("And reveal the songs that we share. 🎶\n")
    lyrics_game = LyricsGame()
    score = 0
    for i in range(3): # play 3 rouds of the game
        guess = lyrics_game.guess_the_lyrics()
        if guess:
            score += 1
    if score >= 2:
        print("Next clue:")
        print(""""
                In a chamber where dreams are softly spun,
                Underneath where your head rests when the day is done.
                Seek a hue of passion, of love, and of fire,
                Beneath the fluff where dreams aspire.

                A box awaits in this cozy nook,
                Underneath where sleepy heads look.
                Its color bold, with tales untold,
                In its confines, a love story to unfold.
              """)
    else:
        print("Get a score of at least 2 to get the next clue!")

























        