from fish_class import *
def fish_info():
    while True:
        key = input("\nEnter key: \n")
        fish_objs = All_fish()
        filtered_fish_objs = fish_objs.find_fish_objects(key)
        for objs in filtered_fish_objs:
            objs.get_species_numbers()
            objs.get_species_info()
            print(objs.json_catch)
if __name__ == "__main__":
    fish_info()