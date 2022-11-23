class GrowthPatternGenerator:
    def __init__(self, growth_pattern_attributes, rng):
        self.growth_pattern_attributes = growth_pattern_attributes
        self.rng = rng

    def __call__(self):
        return {'key': 'nothing'}
