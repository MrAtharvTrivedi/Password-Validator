# Password Strength Analyzer

A GUI-based password strength analyzer built with Python and CustomTkinter. The application evaluates password security based on industry-standard password policy requirements and provides actionable recommendations to help users create stronger credentials.

## Features

* Password strength scoring system
* Checks for minimum password length
* Detects uppercase and lowercase characters
* Validates the presence of numeric characters
* Detects special characters
* Common password detection using a 100,000-password dataset
* Real-time password strength meter
* Security recommendations for weak passwords
* Simple and user-friendly graphical interface

## Technologies Used

* Python 3
* CustomTkinter
* File Handling
* String Processing

## How It Works

The application evaluates a password against the following criteria:

* Minimum length of 12 characters
* Contains at least one uppercase letter
* Contains at least one lowercase letter
* Contains at least one number
* Contains at least one special character
* Is not present in a database of commonly used passwords

Based on the evaluation, the password is assigned a strength rating ranging from **Very Weak** to **Very Strong**.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mratharvtrivedi/password-validator.git
```

2. Navigate to the project directory:

```bash
cd password-validator
```

3. Install dependencies:

```bash
pip install customtkinter
```

4. Run the application:

```bash
python main.py
```

## Project Goals

This project was developed to strengthen Python programming skills while exploring cybersecurity concepts such as password policies, credential security, input validation, and secure password practices.

## Future Improvements

* Password entropy calculation
* Password breach detection using public datasets
* Password generation functionality
* Exportable security reports
* Advanced password policy customization

## Disclaimer

This project is intended for educational and learning purposes only.
