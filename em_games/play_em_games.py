from lyrem import LyricsGame
from wordem import play_wordle
from quizem import QuizGame

if __name__ == "__main__":
    lyrics_game = LyricsGame()
    for i in range(3): # play 3 rouds of the game
        lyrics_game.guess_the_lyrics()
    
    
    quiz_game = QuizGame()
    quiz_game.start_game()
    
    play_wordle()
