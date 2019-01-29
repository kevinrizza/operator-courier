from unittest import TestCase
import pytest
import yaml
from operatorcourier import api

@pytest.mark.parametrize('dir,expected', [
("tests/test_files/valid_bundles/bundle1", "tests/test_files/valid_bundles/results/bundle.1.yaml"),
("tests/test_files/valid_bundles/bundle2", "tests/test_files/valid_bundles/results/bundle.2.yaml"),
])
def test_make_bundle(dir, expected):
    bundle = api.build_and_verify(source_dir=dir)

    with open(expected, "r") as expected_file:
        expected_bundle = yaml.load(expected_file)
        assert bundle == expected_bundle
