from fileinput import close
import random
from cv2 import sort
from numpy import ndarray

def main():
    for i in range(10):
        tournament(15)



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
    xp = 1000
    lv = 1
    test_num = 0




def d(number):
    d6 = random.randint(1,number)
    return d6

def status_screen(character):
    status_screen = f'''
    Name: {character.test_num}
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
        combatant.HP = (combatant.lv * 10) + combatant.CON * 10
        combatant.AC = 10 + combatant.DEX + combatant.WIS

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
    damage = attacker.STR + d(4)
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
            combatant2.xp += combatant1.xp
            level_up(combatant2)
            return combatant2
        if combatant2.HP <= 0:
            combatant1.xp += combatant2.xp
            level_up(combatant1)
            return combatant1

def tournament(rounds):
    number_of_contestants = 2**rounds
    contestants = []
    
    for number in range(number_of_contestants):
        contestant = human()
        contestant.test_num = number
        contestants.append(contestant)
    
    champion = combat_round(number_of_contestants,contestants,rounds)
    print(status_screen(champion))



    
def combat_round(number_of_contestants,contestants,rounds):
    winners = []
    final_tally = []
    for num in range(int(number_of_contestants/2)):
        number = num*2
        winner = fight(contestants[number],contestants[number+1])
        winners.append(winner)
    for person in winners:
        final_tally.append(person)
    if rounds != 1:
        rounds -= 1
        return combat_round(number_of_contestants=len(final_tally),contestants=final_tally,rounds=rounds)
    else:
        return winner
            

        

        

        





if __name__ == "__main__":
    main()