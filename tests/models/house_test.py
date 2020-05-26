import pytest
from src.models.house import massiveHouse

def test_new_massive_house():
    new_massive_house = massiveHouse()
    assert new_massive_house.maxRooms == 28