from collections import defaultdict


class StemGenerator:
    def __init__(self, stem_attributes, rng):
        self.stem_attributes = stem_attributes
        self.rng = rng

    def _clamped_float_avg_std(self, key, avg='avg', std='dsd', min='min', max='max'):
        return self._clamp(self.rng.normalvariate(key[avg], key[std] / 2), key[min], key[max])
    
    def _rng_probability_check(self, key, probability='probability'):
        return self.rng.random() <= key[probability]
    
    def _clamp(self, value, lower, upper):
        return max(min(value, upper), lower)
    
    def validate_attributes(self):
        """Check that the keys and values of the attributes match what this generator knows how to generate"""
        attrs = self.stem_attributes
        assert 'length' in attrs
        assert 'avg' in attrs['length']
        assert 'dsd' in attrs['length']
        assert 'min' in attrs['length']
        assert 'max' in attrs['length']
        assert 'thickness' in attrs
        assert 'avg' in attrs['thickness']
        assert 'dsd' in attrs['thickness']
        assert 'min' in attrs['thickness']
        assert 'max' in attrs['thickness']
        assert 'curviness' in attrs
        assert 'avg' in attrs['curviness']
        assert 'dsd' in attrs['curviness']
        assert 'min' in attrs['curviness']
        assert 'max' in attrs['curviness']
        if 'skirt' in attrs:
            assert 'probability' in attrs['skirt']
            assert 'height' in attrs['skirt']
            assert 'avg' in attrs['skirt']['height']
            assert 'dsd' in attrs['skirt']['height']
            assert 'min' in attrs['skirt']['height']
            assert 'max' in attrs['skirt']['height']
        if 'spore_ring' in attrs:
            assert 'probability' in attrs['spore_ring']
            assert 'height' in attrs['spore_ring']
            assert 'avg' in attrs['spore_ring']['height']
            assert 'dsd' in attrs['spore_ring']['height']
            assert 'min' in attrs['spore_ring']['height']
            assert 'max' in attrs['spore_ring']['height']


    def __call__(self):
        self.validate_attributes()
        attrs = self.stem_attributes
        stem = defaultdict(lambda: dict())
        stem['length'] = self._clamped_float_avg_std(attrs['length'])
        stem['thickness'] = self._clamped_float_avg_std(attrs['thickness'])
        stem['curviness'] = self._clamped_float_avg_std(attrs['curviness'])
        if 'skirt' in attrs:
            if self._rng_probability_check(attrs['skirt']):
                stem['skirt']['height'] = self._clamped_float_avg_std(attrs['skirt']['height'])
        if 'spore_ring' in attrs:
            if self._rng_probability_check(attrs['spore_ring']):
                stem['spore_ring']['height'] = self._clamped_float_avg_std(attrs['spore_ring']['height'])
        return stem
        
