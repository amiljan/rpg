from fileinput import close
import random

from cv2 import sort
from numpy import ndarray


class human:
    HP = 10
    AC = 10
    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0
    move = 1
    mana = 0
    xp = 500
    lv = 1




def d(number):
    d6 = random.randint(1,number)
    return d6

def status_screen(character):
    status_screen = f'''
    HP: {character.HP}
    AC: {character.AC}
    STR: {character.STR}
    DEX: {character.DEX}
    CON: {character.CON}
    INT: {character.INT}
    WIS: {character.WIS}
    CHA: {character.CHA}
    move: {character.move}
    mana: {character.mana}
    xp: {character.xp}
    lv: {character.lv}
    '''
    return status_screen


def xp_to_next_level(level):
    total_xp_to_next_level = 0
    while level > 0:
        xp_for_current = level * 1000
        total_xp_to_next_level += xp_for_current
        level -= 1
    return total_xp_to_next_level

def level_up(combatant):
    if combatant.xp >= xp_to_next_level(combatant.lv):
        combatant.lv +=1
        stats = ["STR","DEX","CON","INT","WIS","CHA"]
        random_stat = random.choice(stats)
        stat_value = getattr(combatant,random_stat)
        setattr(combatant,random_stat,stat_value + 1)
        combatant.HP = (combatant.lv * 10) + combatant.CON
        combatant.AC = 10 + round((combatant.DEX + combatant.WIS)/2,0)

def initiative(combatant1, combatant2):
    roll1 = combatant1.move + d(20)
    roll2 = combatant2.move + d(20)
    if roll1 == roll2:
        initiative(combatant1, combatant2)
    if roll1 > roll2:
        goes_first = 1
    else:
        goes_first = 2
    return goes_first

def melee_attack(attacker,defender):
    to_hit = attacker.DEX + d(20)
    damage = defender.STR + d(4)
    AC = defender.AC
    if to_hit >= AC:
        defender.HP -= damage


def fight(combatant1,combatant2):

    while combatant1.HP > 0 and combatant2.HP > 0:
        ini = initiative(combatant1,combatant2)
        if ini == 1:
            melee_attack(combatant1,combatant2)
        else:
            melee_attack(combatant2,combatant1)
        if combatant1.HP <= 0:
            combatant2.xp += combatant1.xp/2
            level_up(combatant2)
            return combatant2
        if combatant2.HP <= 0:
            combatant1.xp += combatant2.xp/2
            level_up(combatant1)
            return combatant1
    



def tournament(rounds):
    number_of_contestants = 2**rounds
    contestants = []
    winners = []
    for number in range(number_of_contestants):
        contestants.append(human())
    

    for num in range(int(number_of_contestants/2)):
        number = num*2
        winner = fight(contestants[number],contestants[number+1])
        print(winner)

    

#tournament(int(input("Number of rounds: ")))

def dmg_tester(diff):


    dmg = 0
    admg = 0
    ddmg = 0


    for i in range(1000):
        normal_hit = d(20)
        hit1 = d(20)
        hit2 = d(20)
        hits = [hit1,hit2]
        advantage = sorted(hits)[1]
        disadvantage = sorted(hits)[0]


        damage = d(8) + 4

        
        if normal_hit >= diff:
            dmg += 1
        if advantage >= diff:
            admg += 1
        if disadvantage >= diff:
            ddmg += 1

    print(admg)
    print(dmg)
    print(ddmg)
    print(f"Difference {(admg - ddmg)/10}")
    print("")


for i in range(21):
    print(i)
    print("+++++")
    dmg_tester(i)