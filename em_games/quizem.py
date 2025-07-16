import time
import random

class QuizGame:
    def __init__(self):
        self.categories = [
            "Sports",
            "Geography",
            "History",
            "Em&Joao",
            "Music",
            "Beuty&Fashion"
        ]

        self.questions = {
            "Sports": [
                {
                    "question": "Which country won the FIFA World Cup in 2018?",
                    "options": ["A. France", "B. Brazil", "C. Germany", "D. Argentina"],
                    "correct_answer": "A"
                },
                {
                    "question": "In which sport would you perform a slam dunk?",
                    "options": ["A. Soccer", "B. Basketball", "C. Tennis", "D. Golf"],
                    "correct_answer": "B"
                },
                {"question": "Who holds the record for the most Grand Slam titles in tennis?", "options": ["A. Roger Federer", "B. Rafael Nadal", "C. Novak Djokovic", "D. Pete Sampras"], "correct_answer": "C"},
                {"question": "What is the national sport of Japan?", "options": ["A. Karate", "B. Sumo Wrestling", "C. Judo", "D. Baseball"], "correct_answer": "B"},
                {"question": "Which country hosted the 2016 Summer Olympics?", "options": ["A. China", "B. Brazil", "C. United Kingdom", "D. Russia"], "correct_answer": "B"},
                {"question": "How many players are there in a rugby league team?", "options": ["A. 11", "B. 13", "C. 15", "D. 18"], "correct_answer": "B"},
                {"question": "Which of these events is NOT in the decathlon?", "options": ["A. Pole Vault", "B. 1500m", "C. 100m Hurdles", "D. Hammer Throw"], "correct_answer": "D"}
            ],
            "Geography": [
                {
                    "question": "What is the capital of Australia?",
                    "options": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"],
                    "correct_answer": "B"
                },
                {
                    "question": "Which river is the longest in the world?",
                    "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
                    "correct_answer": "A"
                },
                {"question": "Which country has the most islands in the world?", "options": ["A. Finland", "B. Indonesia", "C. Sweden", "D. Philippines"], "correct_answer": "C"},
                {"question": "What is the smallest country in the world?", "options": ["A. Monaco", "B. Nauru", "C. Tuvalu", "D. Vatican City"], "correct_answer": "D"},
                {"question": "Mount Everest is located in which country?", "options": ["A. Nepal", "B. China", "C. India", "D. Tibet"], "correct_answer": "A"},
                {"question": "What is the largest desert in the world?", "options": ["A. Sahara", "B. Arabian", "C. Gobi", "D. Kalahari"], "correct_answer": "A"},
                {"question": "Which U.S. state is known as the 'Sunshine State'?", "options": ["A. California", "B. Florida", "C. Hawaii", "D. Texas"], "correct_answer": "B"}
            ],
            "History": [
                {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "options": ["A. Bessie Coleman", "B. Harriet Quimby", "C. Amelia Earhart", "D. Valentina Tereshkova"], "correct_answer": "C"},
                {"question": "In which year did the Berlin Wall fall?", "options": ["A. 1987", "B. 1989", "C. 1991", "D. 1994"], "correct_answer": "B"},
                {"question": "Which civilization is known for inventing the wheel?", "options": ["A. Roman", "B. Egyptian", "C. Sumerian", "D. Indus Valley"], "correct_answer": "C"},
                {"question": "Who was the first Emperor of Rome?", "options": ["A. Julius Caesar", "B. Nero", "C. Augustus", "D. Caligula"], "correct_answer": "C"},
                {"question": "What year did the Titanic sink?", "options": ["A. 1910", "B. 1912", "C. 1914", "D. 1916"], "correct_answer": "B"}
            ],
            "Em&Joao": [
                {"question": "Where was our first date?", "options": ["A. Bastards Cafe", "B. Student House", "C. Fabro", "D. Disguting food museum"], "correct_answer": "A"},
                {"question": "How long until Em met Joao's whole family?", "options": ["A. One month", "B. Two months", "C. Four months", "D. Eight motnhs"], "correct_answer": "B"},
                {"question": "What is Joao's favorite food?", "options": ["A. Grilled salmon with roasted potatoes", "B. Ricotta & spinach lasagna", "C. Flæskesteg", "D. Vodka pasta"], "correct_answer": "A"},
                {"question": "How much has Joao donated to the pringado box?", "options": ["A. <200DKK", "B. 200-500DKK", "C. 500-800DKK", "D. >800DKK"], "correct_answer": "C"},
                {"question": "How much has Em donated to the pringado box?", "options": ["A. <200DKK", "B. 200-500DKK", "C. 500-800DKK", "D. >800DKK"], "correct_answer": "A"}
            ],
            "Music": [
                {"question": "Who is known as the 'King of Pop'?", "options": ["A. Elvis Presley", "B. Michael Jackson", "C. Justin Timberlake", "D. Prince"], "correct_answer": "B"},
                {"question": "Which band wrote 'Stairway to Heaven'?", "options": ["A. The Beatles", "B. Led Zeppelin", "C. Pink Floyd", "D. The Rolling Stones"], "correct_answer": "B"},
                {"question": "What was Madonna's first top hit?", "options": ["A. Like a Virgin", "B. Material Girl", "C. Holiday", "D. Vogue"], "correct_answer": "C"},
                {"question": "Which musical instrument did Prince famously play?", "options": ["A. Guitar", "B. Drums", "C. Piano", "D. Bass"], "correct_answer": "A"},
                {"question": "Who won the first American Idol?", "options": ["A. Kelly Clarkson", "B. Justin Guarini", "C. Carrie Underwood", "D. Ruben Studdard"], "correct_answer": "A"}
            ],
            "Beuty&Fashion": [
                {"question": "What is the name of the famous little black dress-wearing actress in 'Breakfast at Tiffany’s'?", "options": ["A. Marilyn Monroe", "B. Audrey Hepburn", "C. Elizabeth Taylor", "D. Grace Kelly"], "correct_answer": "B"},
                {"question": "Which luxury fashion house was founded in France in 1854?", "options": ["A. Chanel", "B. Louis Vuitton", "C. Hermes", "D. Gucci"], "correct_answer": "B"},
                {"question": "What is contouring in makeup?", "options": ["A. A technique to highlight", "B. A technique to shape the face", "C. A way to apply blush", "D. A method for eye makeup"], "correct_answer": "B"},
                {"question": "Which country is known for pioneering the 'K-beauty' trend?", "options": ["A. Japan", "B. South Korea", "C. China", "D. Thailand"], "correct_answer": "B"},
                {"question": "Who was the first woman to run a major fashion house?", "options": ["A. Coco Chanel", "B. Donatella Versace", "C. Vivienne Westwood", "D. Miuccia Prada"], "correct_answer": "A"}
            ],
            # Add more categories and questions as needed
        }

        self.score = 0
        self.timer_duration = 30  # Time to answer each question in seconds

    def shuffle_options(self, options):
        random.shuffle(options)

    def display_categories(self):
        print("Choose a category:")
        for i, category in enumerate(self.categories, start=1):
            print(f"{i}. {category}")
        category_choice = int(input("Enter the number of your chosen category: "))
        return self.categories[category_choice - 1]

    def display_question(self, category, question):
        print(f"\n{category} Question:")
        print(question["question"])
        for option in question["options"]:
            print(option)

    def start_game(self):
        print("Welcome to the Quiz Game!")
        selected_category = self.display_categories()

        for _ in range(3):  # Let's ask 3 questions per category
            question = random.choice(self.questions[selected_category])
            self.shuffle_options(question["options"])
            self.display_question(selected_category, question)

            start_time = time.time()
            user_answer = input("Your answer: ").upper()

            if time.time() - start_time > self.timer_duration:
                print("Time's up! You took too long to answer.")
            elif user_answer == question["correct_answer"]:
                print("Correct! +2 points")
                self.score += 2
            else:
                print("Incorrect. -1 point")

            time.sleep(1)

        print(f"\nQuiz completed! Your final score is: {self.score}")
        if self.score >= 5: # Minimum score to get the clue
            print("Find the next clue in the bathroom. Check for a living thing!")
        else:
            print("Play again and get a score of at least 5 to get the next clue!")


if __name__ == "__main__":
    print("\n🌍 Across the lands, through time and space,")
    print("Questions await, a knowledge race.")
    print("From history's depth to the present's grace,")
    print("Start the quiz, and take your ace. 📚\n")
    quiz_game = QuizGame()
    quiz_game.start_game()



































    