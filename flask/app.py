from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*":{'origin': "*"}})

@app.route('/', methods=["GET"])
def hello():
    return "To my anime list"

@app.route('/miaow', methods=["GET"])
def miaow():
    return "You found cat not anime"

ANIME = [{'title':'Fairy Tail', 'tags': {'shounen','comedy'}, 'finished': True}]

@app.route('/anime', methods=["GET", "POST"])
def anime():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        ANIME.append({
            'title': post_data.get('title'),
            'tags': post_data.get('tags'),
            'finished': post_data.get('finished'),
        })
        response_object['message'] = 'Anime added'
    else:
        response_object['anime'] = ANIME
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
