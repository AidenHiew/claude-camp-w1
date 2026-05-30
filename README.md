# Claude Camp Week 1

This repository contains my Week 1 Python and web development practice projects from Claude Camp.

The purpose of this repo is to practise beginner programming concepts through small Python scripts and a simple Flask weather web application.

## Projects Included

### Python Practice Exercises

The Python scripts in this repository practise core programming fundamentals, including:

* Printing output to the terminal
* Taking user input
* Using variables and data types
* Performing calculations
* Writing simple functions
* Using conditionals
* Importing Python standard library modules
* Building small command-line programs

### Flask Weather App

This repository also includes a simple Flask web application that allows a user to search for current weather information by city.

The app uses:

* Flask for the web application
* HTML templates for the user interface
* Requests for API calls
* Open-Meteo for geocoding and weather data

## Suggested Repository Structure

```text
claude-camp-w1/
├── README.md
├── .gitignore
├── requirements.txt
├── app.py
├── templates/
│   ├── index.html
│   └── weather.html
└── exercises/
    ├── calculator.py
    ├── say_hello.py
    ├── greeting_prompt.py
    ├── bmi_calculator.py
    ├── tip_calculator.py
    ├── temperature_converter.py
    └── simple_password_generator.py
```

## Exercise Summary

| File                                     | Description                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------- |
| `exercises/calculator.py`                | Basic calculator practice using numbers, input, and arithmetic operations.              |
| `exercises/say_hello.py`                 | Simple greeting script that asks for the user's name and prints a personalised message. |
| `exercises/greeting_prompt.py`           | Introductory user input exercise that asks for name and age.                            |
| `exercises/bmi_calculator.py`            | Calculates Body Mass Index using weight and height inputs.                              |
| `exercises/tip_calculator.py`            | Calculates a tip amount based on meal cost and tip percentage.                          |
| `exercises/temperature_converter.py`     | Converts Fahrenheit to Celsius.                                                         |
| `exercises/simple_password_generator.py` | Generates a random password using letters, numbers, and symbols.                        |

## Weather App

The weather app allows users to:

* Enter a city name
* Look up the location
* Retrieve current weather data
* Display temperature, weather description, and wind speed

### Run the Weather App

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app.py
```

Then open the local Flask address shown in the terminal.

## Run the Python Exercises

From the project root, run any exercise using Python:

```bash
python exercises/calculator.py
```

```bash
python exercises/say_hello.py
```

```bash
python exercises/bmi_calculator.py
```

```bash
python exercises/tip_calculator.py
```

```bash
python exercises/temperature_converter.py
```

```bash
python exercises/simple_password_generator.py
```

## Learning Goals

This repo demonstrates early practice in:

* Python syntax
* User input and terminal output
* Simple arithmetic calculations
* Conditional logic
* Functions
* Random password generation
* Basic Flask routing
* Rendering HTML templates
* Calling external APIs
* Managing a project with Git and GitHub

## Notes

This is a learning repository. The code is intentionally simple and reflects early-stage programming practice.

Future improvements may include:

* Renaming files using lowercase `snake_case`
* Moving all practice scripts into an `exercises/` folder
* Improving error handling
* Adding comments and docstrings
* Adding screenshots for the weather app
* Improving the web app layout
