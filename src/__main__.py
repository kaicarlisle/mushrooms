import json

from species_attributes_generator import SpeciesGenerator
from individual_attributes_generators import MushroomGenerator



def gen_new_species_attributes(spore=None, output=True):
    species_generator = SpeciesGenerator(spore)
    attributes = species_generator.generate_new_species()
    print(f"spore {species_generator.spore}")
    if output:
        print(json.dumps(attributes, indent=4))
    return species_generator.spore, attributes


def gen_new_mushroom(spore, species_attrs, mushroom_id=None, output=True):
    mushroom_generator = MushroomGenerator(spore, mushroom_id)
    attributes = mushroom_generator.generate_new_mushroom(species_attrs)
    print(f"id {mushroom_generator.id}")
    if output:
        print(json.dumps(attributes, indent=4))
    # to go to point generator
    # to go to renderer
    return mushroom_generator.id, attributes


if __name__ == "__main__":
    mushroom_generator = MushroomGenerator()
    attrs = mushroom_generator.generate_new_mushroom()


    print(f"spore {mushroom_generator.spore}")
    print(json.dumps(mushroom_generator.species_attributes, indent=4))
    print(json.dumps(attrs, indent=4))