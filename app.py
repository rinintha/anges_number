from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
    
    return render_template('index.html', message='')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['attempts'] += 1
    number = session['number']

    if guess < number:
        message = "Too low!"
    elif guess > number:
        message = "Too high!"
    else:
        message = f"Good job! You guessed the number in {session['attempts']} attempts. I'm proud of you!"
        session.pop('number', None)
        session.pop('attempts', None)
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
