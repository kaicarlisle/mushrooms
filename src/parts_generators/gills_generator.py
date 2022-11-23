class GillsGenerator:
    def __init__(self, gills_attributes, rng):
        self.gills_attributes = gills_attributes
        self.rng = rng

    def __call__(self):
        return {'key': 'nothing'}
