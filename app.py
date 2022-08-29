import flask
from flask_cors import *
from fish_class import *
app = flask.Flask(__name__)
CORS(app)
@app.route("/findspecies/", methods={"GET"})
def find_species():
    try:
        species_name = str(flask.request.args.get("specieskey")).replace("_", " ")
    except:
        return flask.jsonify("inncorrect URL argument given")
    fish_objs = All_fish()
    fish_objs.find_fish_objects(species_name)
    fish_objs.create_api_response()
    return flask.jsonify(fish_objs.fish_json_list)

@app.route("/specienumbers", methods={"POST"})
def get_specie_numbers():
    try:
        species = flask.request.get_json()
        fish_obj = Fish(species["Name"], species["Code"], species["Scientific Name"])
        fish_obj.get_species_numbers()
        return flask.jsonify(fish_obj.json_catch)
    except:
        return flask.jsonify("inncorrect body given")

if __name__ == "__main__":
    app.run()
