import pytest
from . import parse_key_file

class TestExtractKeys:

    def test_normal_file(self):
        assert parse_key_file.extract_auth_keys("normal1.txt")==("thisisnormal1id1234", "thisisnormal1key1234")
        assert parse_key_file.extract_auth_keys("normal2.txt")==("cat", "dog")
        assert parse_key_file.extract_auth_keys("oneline.txt")==("nothing", "")
        # file only one line, file with no id/key only title