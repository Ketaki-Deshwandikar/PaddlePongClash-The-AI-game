from flask import Flask, render_template, redirect, url_for
#web application framework written in py
import os #provides functions for interacting with OS

app = Flask(__name__)#creates an instance of the Flask class and assigns it to the variable app

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/play_game')
def play_game():
    os.system('python trial_pong.py')  
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
