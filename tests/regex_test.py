import re
import pytest
import meemoo_metadata_util

def get_testvalues(datatype, key):
    if key in datatype:
        return datatype[key]
    return []

for name, datatype in meemoo_metadata_util.datatypes.items():
    if "regex" in datatype:
        my_regex = re.compile(datatype["regex"])

        @pytest.mark.parametrize('pos_str', get_testvalues(datatype, "pos_test"))
        def test_pos_regex(pos_str):
            assert my_regex.match(pos_str) is not None

        @pytest.mark.parametrize('neg_str', get_testvalues(datatype, "neg_test"))
        def test_neg_regex(neg_str):
            assert my_regex.match(neg_str) is None