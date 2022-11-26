from collections import defaultdict

from parts_generators.generator import Generator


class StemGenerator(Generator):
    def __init__(self, stem_attributes, rng):
        super().__init__(rng)
        self.attrs = stem_attributes

    def validate_attributes(self):
        """Check that the keys and values of the attributes match what this generator knows how to generate"""
        assert "length" in self.attrs
        assert "avg" in self.attrs["length"]
        assert "dsd" in self.attrs["length"]
        assert "min" in self.attrs["length"]
        assert "max" in self.attrs["length"]
        assert "thickness" in self.attrs
        assert "avg" in self.attrs["thickness"]
        assert "dsd" in self.attrs["thickness"]
        assert "min" in self.attrs["thickness"]
        assert "max" in self.attrs["thickness"]
        assert "curviness" in self.attrs
        assert "avg" in self.attrs["curviness"]
        assert "dsd" in self.attrs["curviness"]
        assert "min" in self.attrs["curviness"]
        assert "max" in self.attrs["curviness"]
        if "skirt" in self.attrs:
            assert "probability" in self.attrs["skirt"]
            assert "height" in self.attrs["skirt"]
            assert "avg" in self.attrs["skirt"]["height"]
            assert "dsd" in self.attrs["skirt"]["height"]
            assert "min" in self.attrs["skirt"]["height"]
            assert "max" in self.attrs["skirt"]["height"]
        if "spore_ring" in self.attrs:
            assert "probability" in self.attrs["spore_ring"]
            assert "height" in self.attrs["spore_ring"]
            assert "avg" in self.attrs["spore_ring"]["height"]
            assert "dsd" in self.attrs["spore_ring"]["height"]
            assert "min" in self.attrs["spore_ring"]["height"]
            assert "max" in self.attrs["spore_ring"]["height"]

    def __call__(self):
        stem = defaultdict(lambda: dict())
        stem["length"] = self._clamped_float_avg_std(self.attrs["length"])
        stem["thickness"] = self._clamped_float_avg_std(self.attrs["thickness"])
        stem["curviness"] = self._clamped_float_avg_std(self.attrs["curviness"])
        if "skirt" in self.attrs:
            if self._rng_probability_check(self.attrs["skirt"]):
                stem["skirt"]["height"] = self._clamped_float_avg_std(
                    self.attrs["skirt"]["height"]
                )
        if "spore_ring" in self.attrs:
            if self._rng_probability_check(self.attrs["spore_ring"]):
                stem["spore_ring"]["height"] = self._clamped_float_avg_std(
                    self.attrs["spore_ring"]["height"]
                )
        return stem
