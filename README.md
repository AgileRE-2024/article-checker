# CARINA: Abstract Structure Recommendation

[![N|Solid](https://automationpanda.com/wp-content/uploads/2017/09/django-logo-negative.png?w=65)](https://www.djangoproject.com/)

## Project Description

CARINA is a web-based application that uses Natural Language Processing (NLP) methods, specifically multiclass text classification, to classify whether the structure of an abstract is correctly formatted. The application processes input abstracts and outputs a semi-structured abstract consisting of five key sections:

- **Background**
- **Objectives**
- **Methods**
- **Results**
- **Conclusions**

### Features

- **Abstract Classification**: Classifies abstracts into predefined labels: Background, Objectives, Methods, Results, and Conclusions.
- **Keyword Matching**: Checks for the presence of specific keywords in the abstract and highlights missing keywords.
- **Word Count Validation**: Ensures that the abstract doesn't exceed the word limit (450 words).
- **Interactive Interface**: Users can input their abstracts and get real-time feedback.
- **Copyable Result**: Users can easily copy the structured analysis result to the clipboard.

### Input

This project expects user to have 3 type of input from their abstract:
   - **Title**
   - **Abstract**
   - **Keywords**

## Tech

- [Django] - based Backend using [[Python](https://www.python.org/)]
- [HTML] - structured the website
- [CSS] - styled the website
- [JavaScript] - made interaction through the website

## Installation Instructions

To set up the project locally, follow the steps below.

### Prerequisites

Ensure that you have the following installed on your machine:

- **Python 3.10** or later
- **pip** (Python package installer)
- **Git** (for version control)

### Step-by-Step Installation

1. **Clone the repository**

   First, clone the repository to your local machine using Git:

   ```bash
   git clone <repository-url>
   cd abstract_checker
2. **Setup Virtual Environment**
   
   Recommended to manage dependencies for this project.
   ```bash
   python -m venv venv
   ```
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   macOS/Linux:
   ```bash:
   source venv/bin/activate
   ```
4. **Install all Dependencies**
   
   You can check the dependencies by running a command on your terminal
   ```bash
   pip install -r requirement.txt
   ```
6. **Setup Database**
   
   The database used is dbSqlite3
   ```bash
   python manage.py migrate
   ```
8. **Run the Server**
   ```bash
   python manage.py runserver
   ```
