import random
import json

from schema import SCHEMA
from config import *


def clean_name(name):
    return name.lstrip("?")


class SpeciesGenerator:
    def __init__(self, spore=None):
        self.spore = self._set_spore(spore)
        self.rng = random.Random(self.spore)

    def _set_spore(self, spore_int):
        """Generate new spore (5 bytes) if not given"""
        if spore_int is None:
            return int.from_bytes(random.randbytes(5), "big")
        else:
            return spore_int

    def _eval_string(self, string, attributes):
        """recursively evaluate a string value from the schema"""
        # work out if it's a range (a..b), options [a, b], ref :attr, const #val, func !func
        if ".." in string:
            parts = string.split("..")
            lower_limit = self._eval_string(parts[0], attributes)
            upper_limit = self._eval_string(parts[1], attributes)
            return round(self.rng.uniform(lower_limit, upper_limit), 3)
        if string.startswith("["):
            options = string.lstrip("[").rstrip("]").replace(" ", "").split(',')
            options_evaled = [self._eval_string(option, attributes) for option in options]
            return self.rng.choice(options_evaled)
        if string.startswith(":"):
            return attributes[string.lstrip(":")]
        if string.startswith("!"):
            # get params from string, evaluate them (there may be #const or :attr for example)
            # the call the function with the evaluated params
            evaled = eval(string.lstrip("!"))
        if string.startswith("#"):
            return eval(string.lstrip("#"))
        
        # it's just a number or a name of another object in the schema
        try:
            return float(string)
        # eg growth pattern will have a value of eg 'cluster'
        # all growth pattern values will be generated, just ignore the ones that aren't 'stem.growth_pattern.cluster'
        except ValueError:
            return string


    def generate_new_species(self, schema=SCHEMA):
        """Take the schema dict, and recursively generate a valid attributes dict."""
        attributes = {}
        for name, attribute in schema.items():
            if (name.startswith("?") and bool(self.rng.getrandbits(1))) or not name.startswith("?"):
                cleaned_name = clean_name(name)
                if isinstance(attribute, dict):
                    attributes[cleaned_name] = self.generate_new_species(attribute)
                else:
                    attributes[cleaned_name] = self._eval_string(attribute, attributes)
        return attributes



if __name__ == '__main__':
    species_generator = SpeciesGenerator(spore=760546252912)
    attributes = species_generator.generate_new_species()
    print(species_generator.spore)
    print(json.dumps(attributes, indent=4))
