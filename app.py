import flask
from flask_cors import *
from fish_class import *
app = flask.Flask(__name__)
CORS(app)


@app.route("/findspecieslist/", methods={"GET"})
def find_species():
    try:
        species_name = str(flask.request.args.get("specieskey")).replace("_", " ")
    except:
        return flask.jsonify("inncorrect URL argument given")
    fish_objs = All_fish()
    all_fish_objs = fish_objs.find_fish_objects(species_name)
    response = fish_objs.create_api_response(all_fish_objs)
    return flask.jsonify(response)


@app.route("/findspeciesdesc/", methods={"GET"})
def find_species_and_info():
    try:
        species_name = str(flask.request.args.get("specieskey")).replace("_", " ")
    except:
        return flask.jsonify("inncorrect URL argument given")
    fish_objs = All_fish()
    filtered_fish_objs = fish_objs.find_fish_objects(species_name)
    for objs in filtered_fish_objs:
        objs.get_species_info()
    response = fish_objs.create_api_response(filtered_fish_objs)
    return flask.jsonify(response)


@app.route("/speciesfullinfo", methods={"POST"})
def get_full():
    try:
        species = flask.request.get_json()
        fish_obj = Fish(species["Name"], species["Code"], species["Scientific Name"])
        fish_obj.get_species_numbers()
        fish_obj.get_species_info()
        return flask.jsonify(fish_obj.json_catch)
    except:
        return flask.jsonify("inncorrect body given")

if __name__ == "__main__":
    app.run()
