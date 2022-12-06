"""
Define how attributes should be generated
a..b means a float value between a and b
[a, b, c] means one of a, b, c
:attr means the value generated for attr
#val means the constant val (defined in config.py)
!func(p1, p2) means the values returned when calling the function func with params
?val means the value is optional
"""
import random


"""
Working with dsd = 2 * standard deviation
It's easier this way
"""

SCHEMA = {
    "stem": {
        "length": {
            "avg": "0..#MAX_STEM_LENGTH_AVG",
            "dsd": "0..:avg",
            "min": "0",
            "max": "#MAX_STEM_LENGTH",
        },
        "thickness": {
            "avg": "0..#MAX_STEM_THICKNESS_AVG",
            "dsd": "0..:avg",
            "min": "0",
            "max": "#MAX_STEM_THICKNESS",
        },
        "curviness": {
            "avg": "0..1",
            "dsd": "0..:avg",
            "min": "0",
            "max": "1",
        },
        "?skirt": {
            "probability": "0..1",
            "height": {
                "avg": "0..1",
                "dsd": "0..:avg",
                "min": "0",
                "max": "1",
            },
        },
        "?spore_ring": {
            "probability": "0..1",
            "height": {
                "avg": "0..1",
                "dsd": "0..:avg",
                "min": "0",
                "max": "1",
            },
        },
    },
    "growth_pattern": {
        "type": "[single, clump, cluster]",
        # all mushrooms from same base
        "type.clump": {
            "avg_count": "1..#MAX_GROWTH_PATTERN_CLUMP_AVG_COUNT",
            "dsd_count": "1..:avg_count",
        },
        # spread around
        "type.cluster": {
            "avg_count": "1..#MAX_GROWTH_PATTERN_CLUSTER_AVG_COUNT",
            "dsd_count": "1..:avg_count",
            "avg_distance": "0.5..#MAX_GROWTH_PATTERN_CLUSTER_AVG_DISTANCE",
        },
    },
    "gills": {
        "type": "[fans, honeycomb]",
        "type.fans": {
            # 0 = attached at base of stem, 1 = attached at top of stem (inside cap)
            "attachment": "0..1",
            "density": "#GILLS_FANS_DENSITY_MIN..1",
            "top_level_count": "3..#GILLS_FANS_TOP_LEVEL_COUNT_MAX",
            "levels": {
                # number of levels of smaller fans between each larger one
                "count": "1..5",
                # size difference between each level
                "reduction_ratio": "0..0.99",
            },
        },
        "type.honeycomb": {
            "density": "#GILLS_HONEYCOMB_DENSITY_MIN..1",
        },
    },
}
