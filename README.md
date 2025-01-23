# Basic User Authentication with Flask

<p align="center">
  <img src="https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Ff0i5oszdj3gwk686xuc0.JPG" alt="Screenshot" />
</p>

This repository contains a basic implementation of user authentication using Flask. The application allows users to log in by verifying their credentials. Below are the instructions to run and test the application.

## Prerequisites

Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/).

Additionally, install Flask using pip if you haven't already:

```bash
pip install flask
```

## Code Overview

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Finds login.html in the templates folder

@app.route('/login', methods=['POST'])
def login():
    # Retrieve form data
    username = request.form['username']
    password = request.form['password']
    
    # Simple validation logic
    if username == 'admin' and password == 'secret':
        return f'Welcome, {username}!'
    else:
        return 'Invalid credentials, please try again.'

if __name__ == '__main__':
    app.run(debug=True)
```

### File Structure

Make sure your project structure looks like this:

```
project_folder/
|-- app.py
|-- templates/
    |-- login.html
```

### Example `login.html`

Create a file named `login.html` inside the `templates` folder with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login Page</h1>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

## Running the Application

Follow these steps to run the application:

1. Navigate to the project directory in your terminal or command prompt.

2. Run the following command:

   ```bash
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Screenshot

Below is a screenshot of the running application:

![127.0.0.1_5000](https://github.com/user-attachments/assets/92148a4a-787e-4ffb-95a9-96b2039d830c)
