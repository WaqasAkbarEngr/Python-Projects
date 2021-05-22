from time import sleep
import random

hori_speed = 0.5
vertical_speed = 0.2
hori_fspeed = 0.2
stacked_crates = random.randint(0,26)

def delay(seconds):
    return sleep(seconds)

def random_position():
    x=random.randint(0,50)
    y=random.randint(0,50)
    z=random.randint(0,19)
    position = [x , y , z]
    return position

def stacker_position_check():

    print("\n!!!Stacker is at position",position,"!!!\n")
    delay(2)

def homing():
    print("\n!!!Stacker is moving to home position!!!\n")
    active = True
    while active:
        for coordinate in range(3):
            if coordinate == 0:
                if position[coordinate] != 0:
                    position[coordinate] = abs ( position[coordinate] - hori_speed )
            if coordinate == 1:
                if position[coordinate] > 0:
                    position[coordinate] = abs ( position[coordinate] - hori_speed )
                if position[coordinate] < 0:
                    position[coordinate] = abs ( position[coordinate] + hori_speed )
            if coordinate == 2:
                if position[2] != 20:
                    if position[2] < 20:
                        position[2] = round((position[2] + vertical_speed),1)
                    if position[2] > 20:
                        position[2] = round((position[2] - vertical_speed),1)
        print("Stacker is homing\t",position)
        delay(0.3)
        if position[0] <= 0 and position[1] <= 0 and position[2] == 20:
            delay(2)
            print("\n!!!Stacker is at home position!!!\n")
            delay(2)
            active = False

def moving2crate():
    active = True
    while active:
        for coordinate in range(3):
            if coordinate <2:
                if position[coordinate] != crate_pos[coordinate]:
                    position[coordinate] = round(abs(position[coordinate] + hori_speed),1)
            if coordinate == 2:
                if position[2] > crate_pos[2]:
                    position[2] = round(abs(position[coordinate] - vertical_speed),1)
        print("Stacker is moving toward crate", position)
        delay(0.3)
        if position[0] >= (crate_pos[0] - 5)  and position[1] >= (crate_pos[1] - 5) and position[2] >= (crate_pos[2]-14):
            delay(1)
            active = False

def fine_movement():
    print("\n!!!Stacker is moving on top of crate !!!\n")
    delay(1)
    active = True
    while active:
        for coordinate in range(3):
            if coordinate < 2:
                if position[coordinate] != crate_pos[coordinate]:
                    position[coordinate] = round(abs(position[coordinate] + hori_fspeed),1)
            if coordinate == 2:
                if position[2] > (crate_pos[2]+2):
                    position[2] = round(abs(position[coordinate] - vertical_speed),1)
        print("Stacker is moving on top of crate", position)
        delay(0.3)
        if position[0] >= crate_pos[0]  and position[1] >= crate_pos[1] and position[2] >= (
        crate_pos[2]+2) :
            delay(2)
            print("\n!!!Stacker is on top of crate!!!\n")
            delay(2)
            active = False

def pickup_crate():
    print("\n!!!Stacker is picking up crate!!!\n")
    delay(1)
    down = True
    up = False
    while down:
        if (position[2] >= (crate_pos[2]-2)) and up == False:
            position[2] = round((position[2] - vertical_speed),1)
            print("Stacker is moving down",position)
            delay(0.3)
        if (position[2] < (20)) and up == True:
            position[2] = round((position[2] + hori_speed),1)
            print("Stacker is lifting crate",position)
            delay(0.3)
            if position[2] >= 20:
                delay(1)
                print("\n!!!Stacker has lifted the crate!!!\n")
                down = False
        if position[2] == (crate_pos[2]-2) and up == False:
            delay(1)
            print("\n!!!Stacker is grabbing crate!!!\n")
            delay(3)
            up = True

def detect_crate():
            delay(1)
            print("\n!!!Stacker is checking if crate is present!!!\n")
            z = 3 * random.randint(1, 3)
            crate_pos = [20, 20, z]
            delay(1)
            print("\n!!!Crate is at position", crate_pos,"!!!\n")
            delay(1)
            return crate_pos

def storage_check():
    print("\n!!!Stacker is looking for available space to place crate!!!\n")
    delay(2)
    for i in range(9):
        if stacked_crates // 3 == i:
            location = [(20 * (3 - (i // 3))), ((((i // 3) * 3) - i) * 10), ((i % 3) * 4)]
    print("\n!!!Available space to place crate is",location,"!!!\n")
    delay(2)
    return location

def moving2destination():
    active = True
    while position[0]!=0:
        position[0] = round((position[0] - hori_speed),1)
        print("Stacker is moving towards destination",position)
        delay(0.3)
    while active:
        for coordinate in range(3):
            if coordinate == 0:
                if position[coordinate] < (destination[coordinate]-5):
                    position[coordinate] = round((position[coordinate] + hori_speed),1)
            if coordinate == 1:
                if position[coordinate] != destination[coordinate]:
                    position[coordinate] = round((position[coordinate] - hori_speed),1)
            if coordinate == 2:
                if position[2] > (14):
                    position[2] = round(abs(position[coordinate] - vertical_speed),1)
        print("Stacker is moving toward destination", position)
        delay(0.3)
        if position[0] == (destination[0] - 5) and position[1] == (destination[1]) and position[2] == (14):
            delay(1)
            active = False

def positioning2drop():
    print("\n!!!Stacker getting in position to drop!!!\n")
    delay(2)
    active = True
    while active:
        if position[0] == destination[0] and position[1] == destination[1] and position[2] == (
                destination[2] + 2):
            print("\n!!!Stacker is on top of destination!!!\n")
            delay(1)
            active = False
        else:
            for coordinate in range(3):
                if coordinate == 0:
                    if position[coordinate] != destination[coordinate]:
                        position[coordinate] = round((position[coordinate] + hori_fspeed ),1)
                        print("Stacker is moving to top of destination", position)
                        delay(0.3)
                if coordinate == 2:
                    if position[2] > (destination[2] + 2):
                        position[2] = round((position[coordinate] - vertical_speed),1)
                    print("Stacker is moving to top of destination", position)
                    delay(0.3)


def dropping_crate(stacked_crates):
    print("\n!!!Stacker is dropping crate!!!\n")
    delay(2)
    down = True
    up = False
    while down:
        if (position[2] >= (destination[2] + 0.4)) and up == False:
            position[2] = round((position[2] - vertical_speed),1)
            print("Stacker is moving down", position)
            delay(0.3)
        if (position[2] < (20)) and up == True:
            position[2] = round((position[2] + hori_speed ),1)
            print("Stacker is moving back up", position)
            delay(0.3)
            if position[2] >= 20:
                homing()
                print("\n!!!Stacker is looking for another crate!!!\n")
                delay(2)
                down = False
        if position[2] == (destination[2] + 0.2):
            delay(2)
            print("\n!!!Stacker is releasing crate!!!\n")
            delay(2)
            up = True

# ------------------------------------------------------------------------------------------------------------------------------

position = random_position()
stacker_position_check()
operating = True
while operating:
    homing()
    crate_pos = detect_crate()
    moving2crate()
    fine_movement()
    pickup_crate()
    destination = storage_check()
    moving2destination()
    positioning2drop()
    dropping_crate(stacked_crates)
    stacked_crates = stacked_crates + 1
    if stacked_crates >= 27:
        delay(2)
        print("\n!!!There is no space to stack another crate!!!\n")
        delay(2)
        print("\n!!!Stacker is being put on standby!!!\n")
        delay(2)
        operating = False

exit = input("Press Any Key To Exit")