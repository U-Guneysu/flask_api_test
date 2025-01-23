from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # login.html dosyasını templates klasöründen bulacak

@app.route('/login', methods=['POST'])
def login():
    # Form verilerini alıyoruz
    username = request.form['username']
    password = request.form['password']
    
    # Şifre doğrulaması ve basit kontrol
    if username == 'admin' and password == 'secret':
        return f'Welcome, {username}!'
    else:
        return 'Invalid credentials, please try again.'

if __name__ == '__main__':
    app.run(debug=True)