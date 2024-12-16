# Quiz Game

## Introduction
The **Quiz Game** is a command-line-based application designed to offer a fun and interactive way to test your knowledge. The game allows players to register, answer a set of multiple-choice questions, and view their scores. It also includes a scoreboard to track scores for all participants.

## Features
- **Player Registration**: Players can register their names before playing the quiz.
- **Quiz Gameplay**: A randomized set of questions is presented with four answer options each.
- **Scoring System**: Players earn points for correct answers, with feedback provided after each question.
- **Scoreboard**: Displays the scores of all players after the quiz ends.
- **File-Based Questions**: Questions are stored in an external file (`questions.txt`) for easy customization.

## How It Works
1. Players are welcomed and asked to register their names.
2. A set of questions is loaded from the `questions.txt` file.
3. Questions are displayed one by one, and players choose their answers by entering the corresponding option number.
4. The player’s score is calculated based on the number of correct answers.
5. The final score is displayed, and a scoreboard shows scores of all participants.

## File Format for Questions
The `questions.txt` file should have questions formatted as follows:
```
Question;Option1;Option2;Option3;Option4;CorrectOptionNumber
```
Example:
```
What is the capital of France?;Paris;London;Berlin;Madrid;1
Which planet is known as the Red Planet?;Venus;Mars;Jupiter;Saturn;2
```
