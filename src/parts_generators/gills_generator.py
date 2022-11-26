from collections import defaultdict

from parts_generators.generator import Generator


class GillsGenerator(Generator):
    def __init__(self, gills_attributes, rng):
        super().__init__(rng)
        self.attrs = gills_attributes

    def validate_attributes(self):
        """Check that the keys and values of the attributes match what this generator knows how to generate"""
        assert "type" in self.attrs
        assert "type.fans" in self.attrs
        assert "attachment" in self.attrs["type.fans"]
        assert "density" in self.attrs["type.fans"]
        assert "top_level_count" in self.attrs["type.fans"]
        assert "levels" in self.attrs["type.fans"]
        assert "count" in self.attrs["type.fans"]["levels"]
        assert "reduction_ratio" in self.attrs["type.fans"]["levels"]
        assert "type.honeycomb" in self.attrs
        assert "density" in self.attrs["type.honeycomb"]

    def _generate_type_fans(self):
        fans = defaultdict(lambda: dict())
        type_attrs = self.attrs["type.fans"]
        fans["attachment"] = type_attrs["attachment"]
        fans["density"] = type_attrs["density"]
        fans["top_level_count"] = type_attrs["top_level_count"]
        fans["levels"]["count"] = type_attrs["levels"]["count"]
        fans["levels"]["reduction_ratio"] = type_attrs["levels"]["reduction_ratio"]
        return fans

    def _generate_type_honeycomb(self):
        honeycomb = defaultdict(lambda: dict())
        type_attrs = self.attrs["type.honeycomb"]
        honeycomb["density"] = type_attrs["density"]
        return honeycomb

    def __call__(self):
        gills = defaultdict(lambda: dict())
        type_lookup = {
            "fans": self._generate_type_fans,
            "honeycomb": self._generate_type_honeycomb,
        }

        gills["type"] = self.attrs["type"]
        gills.update(type_lookup[self.attrs["type"]]())
        return gills
