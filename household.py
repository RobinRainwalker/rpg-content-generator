import random
import string
import names
from anytree import Node, RenderTree
from house import *

test = "test"
class Person:
    def __init__(self):
        self.test = test

class Household:
    def __init__(self):
        householdMembers = 0
    #     familyName = names.get_last_name()
    #     self.familyName = familyName
    #     self.householdMembers = householdMembers

    #     print(self.familyName)
    newSmallHouse = smallHouse()
    rooms = newSmallHouse.finalRoomList
    print(newSmallHouse.finalRoomList)
    print(newSmallHouse.roomNumber)

    def createFamilyName(self):
        self.familyName = names.get_last_name()
        print(self.familyName)

        
#head1
#head2(?)
#grandparent(s)?
#children(?)
#dynamic generation based on(?)number of bedrooms? 
newHousehold = Household()
newHousehold.createFamilyName()

#need to generate # of people in a given household (sm, med, big, lg)
#need to generate relationships
#need to generate name/traits for given people

# NAME_GENERATOR
# source: https://github.com/treyhunner/names
# familyName = names.get_last_name()
# femaleFirstName = names.get_first_name(gender='female')
# maleFirstName = names.get_first_name(gender='male')
# print(femaleFirstName + ' ' + familyName)
# print(maleFirstName + ' ' + familyName)

# FAMILY_TREE_GENERATOR
# https://anytree.readthedocs.io/en/2.8.0/