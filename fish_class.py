import requests
import json
import re
class Fish:
    def __init__(self, eng_name, a3_code, sci_name):
        self.name = eng_name
        self.code = a3_code
        self.latin = sci_name
        self.json_catch = {"Name": self.name,
                           "Code": self.code,
                           "Scientific Name": self.latin
                           }
    def get_species_info(self):
        try:
            species_info = json.loads(requests.get(f"https://www.fishwatch.gov/api/species/{self.name}").text)
            self.species_json_info = {"Physical Description": species_info[0]["Physical Description"],
                                      "Species Photo": species_info[0]['Species Illustration Photo']["src"]
                                      }
        except:
            self.species_json_info = None
        self.json_catch["Species Info"] = self.species_json_info
    def get_species_numbers(self):
        try:
            self.specie_numbers = json.loads(requests.get(f"http://openfisheries.org/api/landings/species/{self.code}.json").text)
        except:
            self.specie_numbers = None
        self.json_catch["Specie Numbers"] = self.specie_numbers



class All_fish:
    def __init__(self):
        self.fish_json_data = json.loads(requests.get("http://openfisheries.org/api/landings/species.json").text)
    def find_fish_objects(self, fish_name):
        fish_list = []
        for fish in self.fish_json_data:
            if fish_name.lower() in fish["english_name"].lower() or fish["scientific_name"].lower() == fish_name.lower():
                fish_name_split = re.split("\(|\)" ,fish["english_name"])
                if len(fish_name_split) > 1:
                    for word_coun in range(0,len(fish_name_split)-1):
                        if "=" in fish_name_split[word_coun]:
                            fish_name_split.pop(word_coun)
                new_fish_name = ""
                for words in fish_name_split:
                    if new_fish_name != "":
                        new_fish_name = new_fish_name + " " + words
                    else:
                        new_fish_name = new_fish_name + words
                if new_fish_name != "":
                    fish_list.append(Fish(new_fish_name, fish["a3_code"], fish["scientific_name"]))
        return fish_list
    def create_api_response(self, obj_list):
        fish_json_list = []
        for fish_obj in obj_list:
            fish_json_list.append(fish_obj.json_catch)
        return fish_json_list
