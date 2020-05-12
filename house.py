#This is a piece of code to generate a household in a medieval setting
import random


#Info:
# size of house, rooms
class House:
    def __init__(house, size, rooms):
        house.size = size
        house.rooms = rooms
        #house.architecture = architecture

    def printHouse(house):
        print("size: ", house.size)
        print("rooms: ", house.rooms)
        #print("architecture: ", house.architecture)

#def generateHouse(houseSize, houseRooms):
    
# Housing options
houseSizes = ["small", "medium", "big", "mansion"]
houseRooms = {
    "small": {
        "min": 0,
        "max": 4
    },
    "medium": {
        "min": 3,
        "max": 7
    },
    "big": {
        "min": 6,
        "max": 12
    },
    "mansion": {
        "min": 11,
        "max": 28
    }
}
houseSizeChoice = random.choice(houseSizes)
houseRoomsChoice = random.randint(houseRooms[houseSizeChoice]["min"],houseRooms[houseSizeChoice]["max"])

newHouse = House(houseSizeChoice, houseRoomsChoice)
newHouse.printHouse()
#test = House("big", 9, "old")
#test.printHouse()





# what are the rooms(?)
# # of people & gender & age & name & profession
# # & types of pets
# household items, food, tools
# something precious
# name the house
# save the output as a text file
