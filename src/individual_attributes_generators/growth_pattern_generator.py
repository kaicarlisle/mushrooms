from collections import defaultdict

from individual_attributes_generators.generator import Generator


class GrowthPatternGenerator(Generator):
    def __init__(self, growth_pattern_attributes, rng):
        super().__init__(rng)
        self.attrs = growth_pattern_attributes

    def validate_attributes(self):
        """Check that the keys and values of the attributes match what this generator knows how to generate"""
        assert "type" in self.attrs
        assert "type.clump" in self.attrs
        assert "count" in self.attrs["type.clump"]
        assert "avg" in self.attrs["type.clump"]["count"]
        assert "dsd" in self.attrs["type.clump"]["count"]
        assert "min" in self.attrs["type.clump"]["count"]
        assert "max" in self.attrs["type.clump"]["count"]
        assert "type.cluster" in self.attrs
        assert "count" in self.attrs["type.cluster"]
        assert "avg" in self.attrs["type.cluster"]["count"]
        assert "dsd" in self.attrs["type.cluster"]["count"]
        assert "min" in self.attrs["type.cluster"]["count"]
        assert "max" in self.attrs["type.cluster"]["count"]
        assert "distance" in self.attrs["type.cluster"]
        assert "avg_distance" in self.attrs["type.cluster"]["distance"]

    def _generate_type_clump(self):
        clump = defaultdict(lambda: dict())
        type_attrs = self.attrs["type.clump"]
        clump["count"] = int(self._clamped_float_avg_std(type_attrs["count"]))
        return clump

    def _generate_type_cluster(self):
        cluster = defaultdict(lambda: dict())
        type_attrs = self.attrs["type.cluster"]
        cluster["count"] = int(self._clamped_float_avg_std(type_attrs["count"]))
        cluster["distance"] = type_attrs["distance"]
        return cluster

    def __call__(self):
        growth_pattern = defaultdict(lambda: dict())
        type_lookup = {
            "single": lambda: {},
            "clump": self._generate_type_clump,
            "cluster": self._generate_type_cluster,
        }

        growth_pattern["type"] = self.attrs["type"]
        growth_pattern.update(type_lookup[self.attrs["type"]]())
        return growth_pattern
