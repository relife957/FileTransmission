# -*- coding: utf-8 -*-
from urllib.parse import unquote
from flask import Flask,jsonify
from other_api import request

app = Flask(__name__)

players_list = request.get_players_list()


# poem = request.poem()
# @app.route('/1627406006')
# def poem():
#     return jsonify(poem)

@app.route('/1627406006/<int:id>')
def idiom(id):
    player_data = ''
    if id < 0 or id >= len(players_list):
        return "id should be within 0 - {0}".format(len(players_list))
    if id < len(players_list):
        player_data = request.get_player_detail(players_list[id])
    return jsonify(player_data)



if __name__ == '__main__':
    app.run()
