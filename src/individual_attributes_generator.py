import random
import json

from species_attribute_generator import gen_new_species
from parts_generators import StemGenerator, GrowthPatternGenerator, GillsGenerator


class MushroomGenerator:
    def __init__(self, spore, id=None):
        self.spore = spore
        self.id = self._set_id(id)
        self.rng = random.Random(self.id)
        self.parts = {}
        self.part_generators = {
            "stem": StemGenerator,
            "growth_pattern": GrowthPatternGenerator,
            "gills": GillsGenerator,
        }

    def _set_id(self, id_int):
        """Generate new mushroom id (5 bytes) if not given"""
        return id_int or int.from_bytes(random.randbytes(5), "big")

    def generate_new_mushroom(self, species_attributes):
        """Take a species attributes, generate the attributes of a new instance of that species"""
        # use parts_generator to call the generator class for each part
        for part, generator in self.part_generators.items():
            gen = generator(species_attributes[part], self.rng)
            gen.validate_attributes()
            self.parts[part] = gen()
        return self.parts


def gen_new_mushroom(spore=None, mushroom_id=None, output=True):
    spore, species_attributes = gen_new_species(spore, output=True)
    mushroom_generator = MushroomGenerator(spore, mushroom_id)
    attributes = mushroom_generator.generate_new_mushroom(species_attributes)
    print(f"id {mushroom_generator.id}")
    if output:
        print(json.dumps(attributes, indent=4))
    # to go to point generator
    # to go to renderer
    return spore, mushroom_generator.id, attributes


if __name__ == "__main__":
    gen_new_mushroom()
