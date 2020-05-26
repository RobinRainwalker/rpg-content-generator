import random

class House:
    ROOM_OPTIONS = ["kitchen", "bedroom", "dining room", "bedroom", "bedroom","workroom", "study"]

    def __init__(self):
        self.min_rooms = 3
        self.max_rooms = 7
        self.rooms = self.calculate_rooms()

    def calculate_num_rooms(self):
        return random.randint(self.min_rooms, self.max_rooms)

    def calculate_rooms(self):
        num_rooms = self.calculate_num_rooms()
        return self.ROOM_OPTIONS[0:num_rooms - 1]


class MassiveHouse(House):
    ROOM_OPTIONS = ["kitchen", "dining room", "bedroom", "bedroom","bedroom","guest bedroom","servant bedroom","study","formal sitting room","privy","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test","test"]

    def __init__(self):
        self.min_rooms = 11
        self.max_rooms = 28

        self.rooms = self.calculate_rooms() 

# class bigHouse:
#     def __init__(self):
#         fullRoomList = ["kitchen", "dining room", "bedroom", "bedroom","bedroom","guest bedroom","study","formal sitting room","privy","test","test","servant bedroom"]
#         minRooms = 6
#         maxRooms = 12
#         roomNumber = random.randint(minRooms, maxRooms)
#         finalRoomList = []
#         self.roomNumber = roomNumber
#         self.roomList = fullRoomList
#         self.minRooms = minRooms
#         self.maxRooms = maxRooms
#         self.finalRoomList = finalRoomList

#         for index in range(roomNumber):
#             finalRoomList.append(fullRoomList[index])

# class medHouse:
#     def __init__(self):
#         fullRoomList = ["kitchen", "bedroom", "dining room", "bedroom", "bedroom","workroom", "study"]
#         minRooms = 3
#         maxRooms = 7
#         roomNumber = random.randint(minRooms, maxRooms)
#         finalRoomList = []
#         self.roomNumber = roomNumber
#         self.roomList = fullRoomList
#         self.minRooms = minRooms
#         self.maxRooms = maxRooms
#         self.finalRoomList = finalRoomList

#         for index in range(roomNumber):
#             finalRoomList.append(fullRoomList[index])
        

# class smallHouse:
#     def __init__(self):
#         fullRoomList = ["kitchen & dining room", "bedroom", "work room", "bedroom"]
#         minRooms = 1
#         maxRooms = 4
#         roomNumber = random.randint(minRooms, maxRooms)
#         finalRoomList = []
#         self.roomNumber = roomNumber
#         self.roomList = fullRoomList
#         self.minRooms = minRooms
#         self.maxRooms = maxRooms
#         self.finalRoomList = finalRoomList

#         for index in range(roomNumber):
#             finalRoomList.append(fullRoomList[index])