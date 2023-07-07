
from curses import can_change_color
from distutils.command.build import build
from re import T
import time
import os
import numpy as np
from colorama import *
import colorama
from src.objects import *
from src.canon import Canon
from src.barbarian import Barbarian
from src.input import input_to
from src.king import King
from src.townhall import Townhall
# from huts import(hut

init(autoreset=True)
print(colorama.ansi.clear_screen())
buildingcordinates = np.full((41, 101), 0, dtype=int)


def set_target(barbarian, buildings):
    minimum = 10000
    for i in buildings:
        #print(barbarian.target)
        #time.sleep(0.1)
        if(abs(barbarian.y - i.y) + abs(barbarian.x - i.x) < minimum and i.health > 0):
            minimum = abs(barbarian.y - i.y) + abs(barbarian.x - i.x)
            barbarian.target = i
            
            


def display():
    for i in range(40):
        for j in range(100):
            print(Fore.RED+Back.WHITE + "\033["+str(i)+";"+str(j)+"H"+" ")

    for i in range(19, 22):
        for j in range(49, 53):
            if townhall.health > 0:
                print(Fore.RED+Back.LIGHTCYAN_EX +
                      "\033["+str(i)+";"+str(j)+"H"+"T")
            buildingcordinates[i][j] = 1000
    for i in range(100):
        for j in range(40):
            for k in range(len(barbarian)):  
                if ((last_barb_spawn == "1" or last_barb_spawn == "2" or last_barb_spawn =="3" ) and i == barbarian[k].x and j == barbarian[k].y and barbarian[k].spawn == True):
                    #print(barbarian[k].x)
                    #print(last_barb_spawn)
                    #time.sleep(1)
                    print(Fore.RED+Back.CYAN+"\033["+str(barbarian[k].y)+";"+str(barbarian[k].x)+"H"+"B")

    print(Fore.RED+Back.CYAN+"\033["+str(king.y)+";"+str(king.x)+"H"+"K")
    if Cannon[0].health > 0:
        print(Fore.RED+Back.CYAN +
              "\033["+str(Cannon[0].y)+";"+str(Cannon[0].x)+"H"+"C")
    buildingcordinates[Cannon[0].y][Cannon[0].x] = 101
    if Cannon[1].health > 0:
        print(Fore.RED+Back.CYAN +
              "\033["+str(Cannon[1].y)+";"+str(Cannon[1].x)+"H"+"C")
    buildingcordinates[Cannon[1].y][Cannon[1].x] = 102
    if Cannon[2].health > 0:
        print(Fore.RED+Back.CYAN +
              "\033["+str(Cannon[2].y)+";"+str(Cannon[2].x)+"H"+"C")
    buildingcordinates[Cannon[2].y][Cannon[2].x] = 103
    if Cannon[3].health > 0:
        print(Fore.RED+Back.CYAN +
              "\033["+str(Cannon[3].y)+";"+str(Cannon[3].x)+"H"+"C")
    buildingcordinates[Cannon[3].y][Cannon[3].x] = 104

    if huts[0].health > 0:
        print(Fore.RED+Back.CYAN+"\033[" +
              str(huts[0].y)+";"+str(huts[0].x)+"H"+"H")
    buildingcordinates[huts[0].y][huts[0].x] = 1
    if huts[1].health > 0:
        print(Fore.RED+Back.CYAN+"\033[" +
              str(huts[1].y)+";"+str(huts[1].x)+"H"+"H")
    buildingcordinates[huts[1].y][huts[1].x] = 2
    if huts[2].health > 0:
        print(Fore.RED+Back.CYAN+"\033[" +
              str(huts[2].y)+";"+str(huts[2].x)+"H"+"H")
    buildingcordinates[huts[2].y][huts[2].x] = 3
    if huts[3].health > 0:
        print(Fore.RED+Back.CYAN+"\033[" +
              str(huts[3].y)+";"+str(huts[3].x)+"H"+"H")
    buildingcordinates[huts[3].y][huts[3].x] = 4

    # print(Fore.RED+Back.LIGHTMAGENTA_EX+"\033[5;22H"+"S")
    # print(Fore.RED+Back.LIGHTMAGENTA_EX+"\033[5;59H"+"S")
    # print(Fore.RED+Back.LIGHTMAGENTA_EX+"\033[5;89H"+"S")


Cannon = []
Cannon.append(canon(2, 25, 10, 100))
Cannon.append(canon(2, 75, 10, 100))
Cannon.append(canon(2, 25, 30, 100))
Cannon.append(canon(2, 75, 30, 100))


barbarian = []
barbarian.append(Barbarian(50, 9, 5, 100, True, False, 0))
barbarian.append(Barbarian(50, 10, 5, 100, True, False, 0))
barbarian.append(Barbarian(50, 11, 5, 100, True, False, 0))
barbarian.append(Barbarian(50, 12, 5, 100, True, False, 0))
barbarian.append(Barbarian(50, 13, 5, 100, True, False, 0))


buildings = []
buildings.append(canon(2, 25, 10, 100))
buildings.append(canon(2, 75, 10, 100))
buildings.append(canon(2, 25, 30, 100))
buildings.append(canon(2, 75, 30, 100))

king = King(30, 11, 11, 100, True)

townhall = Townhall(6, 2, 150, True)

buildings.append(Townhall(6, 2, 150, True))
barb_spawning = 0
last_barb_spawn = 0

huts = []
huts.append(hut(3, 3, 50))
huts.append(hut(25, 20, 50))
huts.append(hut(51, 32, 50))
huts.append(hut(88, 24, 50))

move1 = 0

buildings.append(hut(3, 3, 50))
buildings.append(hut(25, 20, 50))
buildings.append(hut(51, 32, 50))
buildings.append(hut(88, 24, 50))
os.system("clear")
last_move = ""
while True:
    # os.system("clear")
    # print(chr(27) + "[2J")a
    # display()
    display()
    
    print(Cannon[0].health)
    
    barb_attack = " "

    barb_spawning = 0

    move = input_to()

    if(move == "1" or move == "2" or move == "3"):
        for i in range(len(barbarian)):
            if(barbarian[i].spawn == False):
                barb_spawning = barb_spawning + 1
                
    if(barb_spawning > 0):
        if(move == '1' or move == '2' or move == '3'):
            last_barb_spawn = move
    
    
    if(move == "w"):
        if(buildingcordinates[king.y-1][king.x] == 0):
            king.y -= 1
        last_move = 'w'
    elif(move == "s"):
        if(buildingcordinates[king.y+1][king.x] == 0):
            king.y = king.y+1
        last_move = 's'
    elif(move == "a"):
        if(buildingcordinates[king.y][king.x-1] == 0):
            king.x = king.x-1
        last_move = 'a'
    elif(move == "d"):
        if(buildingcordinates[king.y][king.x+1] == 0):
            king.x = king.x+1
            if king.y == 10 and king.x == 24:
                print("YES")
                
        last_move = 'd'
    elif (move == " "):
        if(last_move == 'w'):
            if king.y == 22 and (king.x == 49 or king.x == 50 or king.x == 51 or king.x == 52):
                townhall.health -= king.damage
                # print(townhall.health)
            for i in range(len(huts)):
                if huts[i].y == king.y-1 and huts[i].x == king.x:
                    # huts[i].update_health(huts[i],king.damage)
                    huts[i].health -= king.damage
            for i in range(len(Cannon)):
                if Cannon[i].y == king.y-1 and Cannon[i].x == king.x:
                    # Canon[i].update_health(Canon[i],king.damage)
                    Cannon[i].health -= king.damage
        if(last_move == 's'):
            if king.y == 18 and (king.x == 49 or king.x == 50 or king.x == 51 or king.x == 52):
                townhall.health -= king.damage

            for i in range(len(huts)):
                if huts[i].y == king.y+1 and huts[i].x == king.x:
                    # huts[i].update_health(huts[i],king.damage)
                    huts[i].health -= king.damage
            for i in range(len(Cannon)):
                if Cannon[i].y == king.y+1 and Cannon[i].x == king.x:
                    # Canon[i].update_health(Canon[i],king.damage)
                    Cannon[i].health -= king.damage
        if(last_move == 'a'):
            if king.x == 53 and (king.y == 19 or king.y == 20 or king.y == 21):
                townhall.health -= king.damage
                # print(townhall.health)
            for i in range(len(huts)):
                if huts[i].x == king.x-1 and huts[i].y == king.y:
                    # huts[i].update_health(huts[i],king.damage)
                    huts[i].health -= king.health
            for i in range(len(Cannon)):
                if Cannon[i].x == king.x-1 and Cannon[i].y == king.y:
                    # Canon[i].update_health(Canon[i],king.damage)
                    Cannon[i].health -= king.damage
        if(last_move == 'd'):
            # print(king.x)
            # print(king.y)
            if king.x == 48 and (king.y == 19 or king.y == 20 or king.y == 21):
                townhall.health -= king.damage
                # print(townhall.health)
                # time.sleep(1)
            for i in range(len(huts)):
                if huts[i].x == king.x+1 and huts[i].y == king.y:
                    huts[i].health -= king.damage
                    # print(huts[i].health)
            for i in range(len(Cannon)):
                if Cannon[i].x == king.x+1 and Cannon[i].y == king.y:
                    # Canon[i].update_health(Canon[i],king.damage)
                    Cannon[i].health -= king.damage
                    # print(Canon[i].health)
                    
    for i in barbarian: 
        #if(i.target == 0 and i.spawn == True):
            #set_target(i, buildings)
        #elif(i.spawn == True and i.target.health <= 0):
            #set_target(i, buildings)
        if i.spawn == True:
            set_target(i,buildings)
            
    for i in barbarian:
        if(i.spawn):
            if(i.y > i.target.y):
                move1 = 'w'
            if(i.x > i.target.x):
                move1 = 'a'
            if(i.y < i.target.y):
                move1 = 's'
            if(i.x < i.target.x):
                move1 = 'd'
            if(move1 == "w"):
                if(buildingcordinates[i.y-1][i.x] == 0):
                    i.y -= 1
                last_move_b = 'w'
            elif(move1 == "s"):
                if(buildingcordinates[i.y+1][i.x] == 0):
                    i.y = i.y+1
                last_move_b = 's'                
            elif(move1 == "a"):
                if(buildingcordinates[i.y][i.x-1] == 0):
                    i.x = i.x-1
                last_move_b = 'a'
            elif(move1 == "d"):
                if(buildingcordinates[i.y][i.x+1] == 0):
                    i.x = i.x+1
                last_move_b = 'd'
            if (barb_attack == " "):
                if(last_move_b == 'w'):
                    if i.y == 22 and (i.x == 49 or i.x == 50 or i.x == 51 or i.x == 52 and townhall.health > 0):
                        townhall.health -= i.damage
                        for j in range(len(buildings)):
                            if buildings[j].x == 6 and buildings[j].y == 2:
                                buildings[j].health -= i.damage
                        # print(townhall.health)
                    for j in range(len(huts)):
                        if huts[j].y == i.y-1 and huts[j].x == i.x and huts[j].health > 0:
                            # huts[i].update_health(huts[i],i.damage)
                            huts[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == huts[j].x and buildings[k].y == huts[j].y:
                                    buildings[k].health -= i.damage
                    for j in range(len(Cannon)):
                        if Cannon[j].y == i.y-1 and Cannon[j].x == i.x and Cannon[j].health > 0:
                            # Canon[i].update_health(Canon[i],i.damage)
                            Cannon[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == Cannon[j].x and buildings[k].y == Cannon[j].y:
                                    buildings[k].health -= i.damage
                if(last_move_b == 's'):
                    if i.y == 18 and (i.x == 49 or i.x == 50 or i.x == 51 or i.x == 52 and townhall.health > 0):
                        townhall.health -= i.damage
                        for j in range(len(buildings)):
                            if buildings[j].x == 6 and buildings[j].y == 2:
                                buildings[j].health -= i.damage

                    for j in range(len(huts)):
                        if huts[j].y == i.y+1 and huts[j].x == i.x and huts[j].health > 0:
                            # huts[i].update_health(huts[i],i.damage)
                            huts[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == huts[j].x and buildings[k].y == huts[j].y:
                                    buildings[k].health -= i.damage
                    for j in range(len(Cannon)):
                        if Cannon[j].y == i.y+1 and Cannon[j].x == i.x and Cannon[j].health > 0:
                            # Canon[i].update_health(Canon[i],i.damage)
                            Cannon[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == Cannon[j].x and buildings[k].y == Cannon[j].y:
                                    buildings[k].health -= i.damage
                if(last_move_b == 'a'):
                    if i.x == 53 and (i.y == 19 or i.y == 20 or i.y == 21) and townhall.health > 0:
                        townhall.health -= i.damage
                        for j in range(len(buildings)):
                            if buildings[j].x == 6 and buildings[j].y == 2:
                                buildings[j].health -= i.damage
                        # print(townhall.health)
                    for j in range(len(huts)):
                        if huts[j].x == i.x-1 and huts[j].y == i.y and huts[j].health > 0:
                            # huts[i].update_health(huts[i],i.damage)
                            huts[j].health -= i.health
                            for k in range(len(buildings)):
                                if buildings[k].x == huts[j].x and buildings[k].y == huts[j].y:
                                    buildings[k].health -= i.damage
                    for j in range(len(Cannon)):
                        if Cannon[j].x == i.x-1 and Cannon[j].y == i.y and Cannon[j].health > 0:
                            # Canon[i].update_health(Canon[i],i.damage)
                            Cannon[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == Cannon[j].x and buildings[k].y == Cannon[j].y:
                                    buildings[k].health -= i.damage
                if(last_move_b == 'd'):
                    # print(i.x)
                    # print(i.y)
                    if i.x == 48 and (i.y == 19 or i.y == 20 or i.y == 21) and townhall.health > 0:
                        townhall.health -= i.damage
                        for j in range(len(buildings)):
                            if buildings[j].x == 6 and buildings[j].y == 2:
                                buildings[j].health -= i.damage
                        # print(townhall.health)
                        # time.sleep(1)
                    for j in range(len(huts)):
                        if huts[j].x == i.x+1 and huts[j].y == i.y and huts[j].health > 0:
                            huts[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == huts[j].x and buildings[k].y == huts[j].y:
                                    buildings[k].health -= i.damage
                            # print(huts[i].health)
                    for j in range(len(Cannon)):
                        if Cannon[j].x == i.x+1 and Cannon[j].y == i.y and Cannon[j].health > 0:
                            # Canon[i].update_health(Canon[i],i.damage)
                            Cannon[j].health -= i.damage
                            for k in range(len(buildings)):
                                if buildings[k].x == Cannon[j].x and buildings[k].y == Cannon[j].y:
                                    buildings[k].health -= i.damage
                            # print(Canon[i].health)
                
    for i in buildings:
        if(i.health <= 0):
            buildingcordinates[i.y][i.x] = 0
            buildings.remove(i)
            print(buildingcordinates[i.y][i.x])
            time.sleep(1)
        

    if(move == "1" and barb_spawning <= 5 and barb_spawning > 0):
        for i in range(len(barbarian)):
            if(barbarian[i].spawn == False):
                barbarian[i].spawn = True
                barbarian[i].x = 22
                barbarian[i].y = 5
                barb_spawning = barb_spawning + 1
                break
            
    if(move == "2" and barb_spawning <= 5 and barb_spawning > 0):
        for i in range(len(barbarian)):
            if(barbarian[i].spawn == False):
                barbarian[i].spawn = True
                barbarian[i].x = 59
                barbarian[i].y = 5
                barb_spawning = barb_spawning + 1
                break
            
    if(move == "3" and barb_spawning <= 5 and barb_spawning > 0):
        for i in range(len(barbarian)):
            if(barbarian[i].spawn == False):
                barbarian[i].spawn = True
                barbarian[i].x = 89
                barbarian[i].y = 5
                barb_spawning = barb_spawning + 1
                break
            
    
    # print(last_move)
    # time.sleep(0.1)
