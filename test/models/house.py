import pytest
from src.models.house import *


# def test_massiveHouse():
#     newMassiveHouse = massiveHouse()
#     assert hasattr(maxrooms, "check")

class TestMassiveHouse:
    def test_new_massive_house(self):
        new_massive_house = massiveHouse()
        assert new_massive_house.maxrooms == 28