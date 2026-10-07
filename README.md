# Python Foundations

A collection of Python exercises completed as part of the Beginner Stage (B1) of an AI Engineering course.

The purpose of this repository is to build a solid Python programming foundation through practical engineering exercises covering variables, conditionals, loops, functions, modules, error handling, file handling, and script organisation.

## Learning Objectives

This project demonstrates the ability to:

* Write readable Python programs.
* Use Python variables and common data types.
* Apply conditional logic and loops.
* Create and reuse functions.
* Organise related functionality into modules.
* Handle errors and invalid input.
* Read and process data from files.
* Structure a small Python application.
* Write automated tests.
* Use Git for version control and maintain meaningful commit history.

## Requirements

* Python 3.11 or newer
* pip
* Git
* pytest

The exercises were developed and tested in a Python virtual environment.

## Project Structure

```text
python-foundations/
│
├── 01_variables/
│   ├── README.md
│   └── student_profile.py
│
├── 02_conditionals/
│   ├── README.md
│   └── grade_classifier.py
│
├── 03_loops/
│   ├── README.md
│   └── score_analyzer.py
│
├── 04_functions/
│   ├── README.md
│   ├── score_utils.py
│   ├── score_report.py
│   └── test_score_utils.py
│
├── 05_modules/
│   ├── README.md
│   ├── calculator.py
│   ├── formatter.py
│   ├── main.py
│   └── test_calculator.py
│
├── 06_error_handling/
│   ├── README.md
│   ├── grade_classifier.py
│   ├── input_utils.py
│   └── test_input_utils.py
│
├── 07_file_handling/
│   ├── README.md
│   ├── data/
│   │   └── students.csv
│   ├── student_reader.py
│   ├── report_generator.py
│   └── test_student_reader.py
│
├── 08_script_organisation/
│   ├── README.md
│   ├── data/
│   │   └── students.csv
│   ├── student_analyzer/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   ├── file_handler.py
│   │   ├── formatter.py
│   │   ├── main.py
│   │   └── models.py
│   └── tests/
│       ├── test_analyzer.py
│       └── test_file_handler.py
│
├── debugging-note.md
├── requirements.txt
└── README.md
```

## Exercise Overview

### 01 - Variables and Data Types

Introduces Python variables and common data types through a student profile and performance calculation.

### 02 - Conditionals

Uses conditional statements to classify student scores into grades and determine pass/fail status.

### 03 - Loops

Uses iteration to analyse multiple student scores and calculate basic statistics.

### 04 - Functions

Extracts reusable score-processing operations into functions and introduces automated testing with pytest.

### 05 - Modules

Builds on the functions exercise by separating calculations, formatting, and application flow into independent Python modules.

### 06 - Error Handling

Introduces exception handling and input validation so programs can respond appropriately to invalid input and runtime errors.

### 07 - File Handling

Reads student information from a CSV file and generates a performance report.

### 08 - Script Organisation

Combines the concepts from the previous exercises into a more structured Student Performance Analyzer application with separate modules and tests.

## Setting Up the Project

Clone the repository:

```bash
git clone <your-github-repository-url>
cd python-foundations
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment on Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```powershell
venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running the Exercises

Each exercise can be run independently.

For example:

```bash
python 01_variables/student_profile.py
```

or:

```bash
python 03_loops/score_analyzer.py
```

For exercises containing modules, run the main application from the appropriate directory.

## Running Tests

Run all automated tests from the project root:

```bash
pytest
```

To run tests for a specific exercise:

```bash
pytest 04_functions/
```

or:

```bash
pytest 05_modules/
```

## Testing

Automated tests are included for multiple exercises.

The tests verify important behaviours such as:

* Score calculations
* Input validation
* File reading
* Data analysis

## Debugging

A debugging note documenting an encountered error, its cause, investigation, and resolution is available in:

```text
debugging-note.md
```

## What I Learned

This project reinforced the difference between writing code that works and writing code that is organised and maintainable.

The exercises progressed from basic Python syntax to reusable functions, modular code, error handling, file processing, testing, and structured application design.

The later exercises also demonstrated the importance of separating responsibilities between different parts of an application.

## Conclusion

This repository represents my practical work for the B1 Python Programming Foundations module and provides the foundation for progressing to more advanced software engineering and AI engineering topics.
