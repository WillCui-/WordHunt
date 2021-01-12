# from src.game import Game
from app import app
from src.game import Game

from flask import request

blank_game = '                '

g = Game(blank_game)
g.deserialize_and_store("serialized_trie.txt")
word_list = []

@app.route('/')
@app.route('/index')
def index():
    return {'message': 'bet'}


@app.route('/letters', methods=['GET', 'POST'])
def letters():
    if request.method == 'GET':
        return {'letters': g.get_board()}
    elif request.method == 'POST':
        letters = request.form.get('letters')
        g.set_board(letters)
        word_list = g.calculate_words
        

@app.route('/results', methods=['GET'])
def results():
    return {'results': word_list}