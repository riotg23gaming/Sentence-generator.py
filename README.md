# Random Sentence Generator

## Description

Random Sentence Generator is a small Python project that creates random sentences by combining different words and phrases. Each sentence can contain a name, an action, an object, a place, and a time.

The project was created to practise Python fundamentals, including lists, functions, loops, conditional statements, user input, and the `random` module.

## Features

- Generate random sentences.
- Choose between Short and Long sentence modes.
- Generate multiple sentences without restarting the program.
- Navigate through a simple menu with Play, Options, and Exit.
- Handle invalid choices in the Options menu.

## How It Works

The program stores names, verbs, objects, places, and time expressions in separate lists. A function uses `random.choice()` to select a random element from a list.

In Short mode, the program generates a sentence using a name, an action, and an object.

In Long mode, it adds a place and a time expression to create a longer sentence.

## Requirements

- Python 3
- No external libraries required.

The project uses Python's built-in `random` and `time` modules.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in your terminal or IDE.
3. Run the Python file.

```bash
python random_sentence_generator.py
```

Replace the filename in the command if your Python file has a different name.

## What I Learned

While working on this project, I practised using lists to store data, writing reusable functions, selecting random elements, controlling program flow with loops and conditions, and building a simple menu-driven application.
