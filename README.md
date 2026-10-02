# 🎯 Number Guessing Game

A simple Python-based **Number Guessing Game** where the computer randomly selects a number between **1 and 100**, and the user tries to guess it. The program provides hints such as **"Too High"** or **"Too Low"** until the correct number is guessed.

## 📌 Problem Description

The objective is to create an interactive game in which:

* The computer generates a random number.
* The user enters guesses.
* The program compares the guess with the generated number.
* The program gives hints when the guess is incorrect.
* The game continues until the user guesses the correct number.

## ⚙️ How the Code Works

The program uses Python's built-in `random` module.

### 1. Generate a Random Number

```python
number = random.randint(1, 100)
```

This generates a random integer between **1 and 100**.

### 2. Take User Input

The program asks the user to enter their guess:

```python
guess = int(input("Enter your guess: "))
```

The input is converted from text into an integer.

### 3. Compare the Guess

The program checks whether the user's guess is:

* **Greater than** the secret number → `Too High`
* **Less than** the secret number → `Too Low`
* **Equal to** the secret number → `Correct`

### 4. Repeat Until Correct

A `while` loop keeps asking the user for another guess until the correct number is found.

```python
while True:
```

When the correct number is guessed, the `break` statement stops the loop.

## 🛠️ Technologies Used

* **Python 3**
* **random module**
* **while loop**
* **if-elif-else conditions**
* **User input**

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

### Step 3: Open the Project Folder

```bash
cd number-guessing-game
```

### Step 4: Run the Program

```bash
python number_guessing_game.py
```

On some systems, use:

```bash
python3 number_guessing_game.py
```

## 🎮 Example Output

```text
Welcome to the Number Guessing Game!
I have chosen a number between 1 and 100.

Enter your guess: 70
Too High! Try again.

Enter your guess: 40
Too Low! Try again.

Enter your guess: 55
Correct! You guessed the number!
```

## 📂 Project Structure

```text
number-guessing-game/
│
├── number_guessing_game.py
└── README.md
```

## 💡 Future Improvements

The game can be improved by adding:

* Number of attempts counter
* Difficulty levels
* Limited number of guesses
* Play-again option
* Input validation
* Score calculation

## 📄 License

This project is created for learning and educational purposes.
