from unittest import TestCase
import pytest
from command.build import BuildCmd


def test_create_bundle():
    paths = ["tests/test_files/csv.yaml", "tests/test_files/crd.yaml", "tests/test_files/package.yaml"]
    yamls = []
    for x in range(3):
        with open(paths[x]) as f:
            yamls.append(f.read())

    bundle = BuildCmd().build_bundle(yamls)
    assert bool(bundle["data"]["packages"]) == True
    assert bool(bundle["data"]["clusterServiceVersions"]) == True
    assert bool(bundle["data"]["customResourceDefinitions"]) == True
