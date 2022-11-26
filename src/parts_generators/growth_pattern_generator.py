from parts_generators.generator import Generator


class GrowthPatternGenerator(Generator):
    def __init__(self, growth_pattern_attributes, rng):
        super().__init__(rng)
        self.attrs = growth_pattern_attributes

    def __call__(self):
        return {"key": "nothing"}

    def validate_attributes(self):
        """Check that the keys and values of the attributes match what this generator knows how to generate"""
        pass
