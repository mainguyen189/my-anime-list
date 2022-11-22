from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*": {'origin': "*"}})


@app.route('/', methods=["GET"])
def hello():
    return "To my anime list"


@app.route('/miaow', methods=["GET"])
def miaow():
    return "You found cat not anime"


ANIME = [{
    'id': uuid.uuid4().hex,
    'title': 'Fairy Tail', 
    'tags': ['shounen', 'comedy'], 
    'finished': True}]

#get and post
@app.route('/anime', methods=["GET", "POST"])
def anime_list():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        ANIME.append({
            'id': uuid.uuid4().hex(),
            'title': post_data.get('title'),
            'tags': post_data.get('tags'),
            'finished': post_data.get('finished'),
        })
        response_object['message'] = 'Anime added'
    else:
        response_object['anime'] = ANIME
    return jsonify(response_object)



#put and delete
@app.route('/anime/<anime_id>', methods=["PUT","DELETE"])
def ani(anime_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        ANIME.append({
            'id': uuid.uuid4().hex(),
            'title': post_data.get('title'),
            'tags': post_data.get('tags'),
            'finished': post_data.get('finished'),
        })
        response_object['message'] = 'Anime updated'
    if request.method == "DELETE":
        remove_anime(anime_id)
        response_object['message'] = 'Anime removed'
    return jsonify(response_object)


def remove_anime(anime_id):
    for ani in ANIME:
        if ani["id"] == anime_id:
            ANIME.remove(ani)
            return True
    return False


if __name__ == "__main__":
    app.run(debug=True)
