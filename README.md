# URL Shortener

A simple URL shortener web application built using Flask and `pyshorteners`. This application allows users to input a long URL and get a shortened version that can be shared more easily.

## Features

- Enter a long URL to get a shortened URL.
- Copy and share the shortened URL.
- Simple and clean user interface with a modern design.

## Requirements

- Python 3.6 or higher
- Flask
- `pyshorteners`

## Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/PrajwalaY26/URL_Shortener.git
   cd url_shortener
   ```
2. **Set Up a Virtual Environment**
    # For Windows
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

  # For macOS/Linux
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
3. **Install Dependencies**
   ```bash
     pip install Flask pyshorteners
   ```
4. **Run the Flask Application**
   ```bash
     python app.py
   ```
5. **Access the Application**
   Open your web browser and go to http://127.0.0.1:5000/. You should see the URL shortener interface.

## Usage
- Enter the long URL in the input field on the home page.
- Click the "Shorten" button.
- The shortened URL will be displayed below the form.
- You can click on the shortened URL to open it in a new tab or copy it for sharing.
