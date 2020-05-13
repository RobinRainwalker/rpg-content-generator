import random

class massiveHouse:
    def __init__(self):
        fullRoomList = ["kitchen", "dining room", "bedroom", "bedroom","bedroom","guest bedroom","servant bedroom","study","formal sitting room","privy","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test"]
        minRooms = 11
        maxRooms = 28
        roomNumber = random.randint(minRooms, maxRooms)
        finalRoomList = []
        self.roomNumber = roomNumber
        self.roomList = fullRoomList
        self.minRooms = minRooms
        self.maxRooms = maxRooms
        self.finalRoomList = finalRoomList


        for index in range(roomNumber):
            finalRoomList.append(fullRoomList[index])

class bigHouse:
    def __init__(self):
        fullRoomList = ["kitchen", "dining room", "bedroom", "bedroom","bedroom","guest bedroom","study","formal sitting room","privy","test","test","servant bedroom"]
        minRooms = 6
        maxRooms = 12
        roomNumber = random.randint(minRooms, maxRooms)
        finalRoomList = []
        self.roomNumber = roomNumber
        self.roomList = fullRoomList
        self.minRooms = minRooms
        self.maxRooms = maxRooms
        self.finalRoomList = finalRoomList


        for index in range(roomNumber):
            finalRoomList.append(fullRoomList[index])

class medHouse:
    def __init__(self):
        fullRoomList = ["kitchen", "bedroom", "dining room", "bedroom", "bedroom","workroom", "study"]
        minRooms = 3
        maxRooms = 7
        roomNumber = random.randint(minRooms, maxRooms)
        finalRoomList = []
        self.roomNumber = roomNumber
        self.roomList = fullRoomList
        self.minRooms = minRooms
        self.maxRooms = maxRooms
        self.finalRoomList = finalRoomList


        for index in range(roomNumber):
            finalRoomList.append(fullRoomList[index])
        

class smallHouse:
    def __init__(self):
        fullRoomList = ["kitchen & dining room", "bedroom", "work room", "bedroom"]
        minRooms = 1
        maxRooms = 4
        roomNumber = random.randint(minRooms, maxRooms)
        finalRoomList = []
        self.roomNumber = roomNumber
        self.roomList = fullRoomList
        self.minRooms = minRooms
        self.maxRooms = maxRooms
        self.finalRoomList = finalRoomList


        for index in range(roomNumber):
            finalRoomList.append(fullRoomList[index])

# newMassiveHouse = massiveHouse()
# newBigHouse = bigHouse()
# newMedHouse = medHouse()
# newSmallHouse = smallHouse()

# print(newMassiveHouse.finalRoomList())
# print(newBigHouse.finalRoomList())
# print(newMedHouse.finalRoomList())
# print(newSmallHouse.finalRoomList())