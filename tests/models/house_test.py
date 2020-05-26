import pytest
from src.models.house import MassiveHouse

def test_new_massive_house():
    new_massive_house = MassiveHouse()
    assert new_massive_house.max_rooms == 28