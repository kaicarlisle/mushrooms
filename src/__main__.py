import json

from individual_attributes_generators import MushroomGenerator


if __name__ == "__main__":
    # Mushroom Generator will accept a spore,
    # or if not given will generate a new species
    # It will generate the attrs dictionary that will be sent to the 3d points generator
    # which will generate points to go to the renderer
    mushroom_generator = MushroomGenerator()
    attrs = mushroom_generator.generate_new_mushroom()

    print(f"spore {mushroom_generator.spore}")
    print(f"id {mushroom_generator.id}")
    # print(json.dumps(mushroom_generator.species_attributes, indent=4))
    print(json.dumps(attrs, indent=4))
