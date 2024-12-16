import random

# Global variables
scores = {}

# Main function
def main():
    print("Welcome to the Quiz Game!")
    print("1. Register and Play\n2. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        player_name = input("Enter your name: ")
        print(f"\nHello, {player_name}! Let's start the quiz.")

        score = start_quiz()
        scores[player_name] = score

        print(f"\nYour final score: {score}")
        display_scoreboard()
    else:
        print("Thank you for visiting! Goodbye.")

# Function to start the quiz
def start_quiz():
    score = 0
    questions = load_questions_from_file("questions.txt")

    if not questions:
        print("No questions available. Please check the file.")
        return score

    random.shuffle(questions)  # Shuffle the questions

    for question in questions:
        print(f"\n{question[0]}")
        for i in range(1, 5):
            print(f"{i}. {question[i]}")

        try:
            answer = int(input("Your answer (1-4): "))
            if answer == int(question[5]):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question[int(question[5])]}.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    return score

# Function to load questions from a file
def load_questions_from_file(file_name):
    questions = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) == 6:
                    questions.append(parts)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return questions

# Function to display the scoreboard
def display_scoreboard():
    print("\nScoreboard:")
    for player, score in scores.items():
        print(f"Player: {player} | Score: {score}")

if __name__ == "__main__":
    main()
