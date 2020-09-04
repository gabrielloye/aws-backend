from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

urls = [
        "https://reports7123.s3.amazonaws.com/energy+sector+report/20200602095540_sgreits_industrial_1Q20+020620+IF.pdf",
        "https://reports7123.s3.amazonaws.com/energy+sector+report/20200812123242_China+Gas+Sector.pdf",
        "https://reports7123.s3.amazonaws.com/energy+sector+report/20200623162758_China+Oil+%26+Gas+Sector_23-Jun-2020_HK_IF.pdf",
        "https://reports7123.s3.amazonaws.com/energy+sector+report/20200728173946_China+Oil+and+Gas+Sector_28-Jul-2020_HK_IF.pdf"
]

@app.route('/')
def landing():
    return "<h1>DBS Dashboard Backend Server</h1>"

@app.route('/recommendreport', methods=["GET", "POST"])
def recommend_report():
    """
    DBS report recommender for headlines
    """
    if request.method == "POST":
        headline = request.json['headline']
    elif request.method == "GET":
        headline = request.args['headline']
    """
    TO-DO:
    - Add Named Entity Recognition model to recognise the key topics in the headline
    - Using the recognised entities, do a search on the database and return a relevant article
    - Sentence similarity score with existing headlines in database?
    """
    return jsonify({
        "url": random.choice(urls),
        "headline": headline
    })

@app.route('/recommendtopic', methods=["GET", "POST"])
def recommend_topic():
    """
    Recommend categories for user dashboard based on past user interactions and information
    """
    pass

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
