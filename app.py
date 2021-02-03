from src.game import Game

from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')
CORS(app)

blank_game = '                '

g = Game(blank_game)
g.deserialize_and_store("serialized_trie.txt")
word_list = []


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/letters', methods=['GET', 'POST'])
def letters():
    if request.method == 'GET':
        return {'letters': g.get_board()}
    elif request.method == 'POST':
        letters = request.form['letters']
        letters = letters.lower()
        g.set_board(letters)
        word_list = g.calculate_words()
        return {'results': word_list}
        

@app.route('/api/results', methods=['GET'])
def results():
    return {'results': word_list}


if __name__ == "__main__":
    app.run()
