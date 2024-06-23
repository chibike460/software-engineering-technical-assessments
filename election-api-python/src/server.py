from flask import Flask, request, jsonify
from results_controller import ResultsController
import os
import json


app: Flask = Flask(__name__)
controller: ResultsController = ResultsController()


# Define the directory containing the JSON files
directory = 'resources/sampleelectionresults/'



# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as json_file:
            # Load the JSON content and append it to the list
            content = json.load(json_file)
            # pprint.pprint(content)
            controller.new_result(content)




@app.route("/")
def index():
    return jsonify({"message": "Homepage"})

@app.route("/result/<id>", methods=["GET"])
def individual_result(id) -> dict:
    return controller.get_result(int(id))

@app.route("/result", methods=["POST"])
def add_result() -> dict:
    return controller.new_result(request.json)

@app.route("/scoreboard", methods=["GET"])
def scoreboard() -> dict:
    return controller.scoreboard()
    