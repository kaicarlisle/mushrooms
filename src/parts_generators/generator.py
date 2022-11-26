class Generator:
    def __init__(self, rng):
        self.rng = rng

    def _rng_uniform(self, lower, upper):
        return self.rng.random() * (upper - lower) + lower

    def _clamped_float_avg_std(self, key, avg="avg", std="dsd", min="min", max="max"):
        return self._clamp(
            self.rng.normalvariate(key[avg], key[std] / 2), key[min], key[max]
        )

    def _rng_probability_check(self, key, probability="probability"):
        return self.rng.random() <= key[probability]

    def _clamp(self, value, lower, upper):
        return max(min(value, upper), lower)

    def validate_attributes(self):
        raise NotImplementedError()

    def __call__(self):
        raise NotImplementedError()
