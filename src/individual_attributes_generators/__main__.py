import random

from species_attributes_generator import SpeciesGenerator
from individual_attributes_generators.stem_generator import StemGenerator
from individual_attributes_generators.growth_pattern_generator import (
    GrowthPatternGenerator,
)
from individual_attributes_generators.gills_generator import GillsGenerator


class MushroomGenerator:
    def __init__(self, spore=None, id=None):
        # Get the species attributes for the given spore, or new attributes if no spore given
        self.species_generator = SpeciesGenerator(spore)
        self.species_attributes = self.species_generator.generate_new_species()
        self.spore = self.species_generator.spore

        self.id = self._set_id(id)
        self.rng = random.Random(self.id)
        self.part_generators = {
            "stem": StemGenerator,
            "growth_pattern": GrowthPatternGenerator,
            "gills": GillsGenerator,
        }

    def _set_id(self, id_int):
        """Generate new mushroom id (5 bytes) if not given"""
        return id_int or int.from_bytes(random.randbytes(5), "big")

    def generate_new_mushroom(self):
        """Take a species attributes, generate the attributes of a new instance of that species"""
        parts = {}
        # use parts_generators to call the generator class for each part
        for part, generator in self.part_generators.items():
            gen = generator(self.species_attributes[part], self.rng)
            gen.validate_attributes()
            parts[part] = gen()
        return parts
