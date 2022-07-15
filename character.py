from fileinput import close
import random
from cv2 import sort
from numpy import ndarray
import csv

def main():
    for i in range(10):
        npc_life(human())



class human:
    NAME = "UNKNOWN"
    CLASS = "NONE"
    HP = 10
    AC = 10
    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0
    gender = "UNKNOWN"
    profession = "NONE"
    xp = 0
    lv = 1
    age = 0
    test_num = 0
    predisposition = "UNKNOWN"
    background = "\n"
    wealth = 0
    generation = 0
    weapon = 1

    move = 0
    mana = 0
        




def d(number):
    d6 = random.randint(1,number)
    return d6

def status_screen(character):
    status_screen = f'''
NAME: {character.NAME}
CLASS: {character.CLASS}
HP: {character.HP}
AC: {character.AC}
STR: {character.STR}
DEX: {character.DEX}
CON: {character.CON}
INT: {character.INT}
WIS: {character.WIS}
CHA: {character.CHA}

lv: {character.lv}
xp: {character.xp} of {xp_to_next_level(character.lv)}
damage: d{character.weapon}
move: {character.move}
mana: {character.mana}
gender: {character.gender}
profession: {character.profession}
age: {character.age}
wealth: {character.wealth}

Background: {character.background}
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
        stats_fight = ["STR","STR","STR","DEX","CON","INT","WIS","CHA"]
        stats_sneak = ["STR","DEX","DEX","DEX","CON","INT","WIS","CHA"]
        stats_cast =  ["STR","DEX","CON","INT","INT","INT","WIS","CHA"]
        stats_heal =  ["STR","DEX","CON","INT","WIS","WIS","WIS","CHA"]
        
        if combatant.predisposition == "fight":
            stats = stats_fight
        if combatant.predisposition == "sneak":
            stats = stats_sneak
        if combatant.predisposition == "cast":
            stats = stats_cast
        if combatant.predisposition == "heal":
            stats = stats_heal
        else:
            stats = ["STR","DEX","CON","INT","WIS","CHA"]
        
        random_stat = random.choice(stats)
        stat_value = getattr(combatant,random_stat)
        setattr(combatant,random_stat,stat_value + 1)
        
        combatant.HP = (combatant.lv * 10) + combatant.CON * 20
        combatant.AC += combatant.DEX + combatant.WIS
        combatant.move = combatant.STR + combatant.DEX + combatant.CON
        combatant.mana = combatant.INT + combatant.DEX + combatant.CHA


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
    damage = attacker.STR + d(attacker.weapon)
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
            combatant2.xp += combatant1.lv * d(1000)
            level_up(combatant2)
            return combatant2
        if combatant2.HP <= 0:
            combatant1.xp += combatant2.lv * d(1000)
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
            
def npc_life(person):
    birth(person)
    print(status_screen(person))



def birth(person):    
    genders = ["male","female"]
    gender = random.choice(genders)
    person.gender = gender
    name = ""
    if gender == "male":
        lines_first = open('first_names_male.txt').read().splitlines()
        first_name = random.choice(lines_first)
        lines_last = open('last_names.txt').read().splitlines()
        last_name = random.choice(lines_last)
        name = f"{first_name} {last_name}"
    if gender == "female":
        lines_first = open('first_names_female.txt').read().splitlines()
        first_name = random.choice(lines_first)
        lines_last = open('last_names.txt').read().splitlines()
        last_name = random.choice(lines_last)
        name = f"{first_name} {last_name}"
    person.NAME = name
    
    predispositions = ["fight","sneak","cast","heal"]
    predisposition = random.choice(predispositions)
    person.predisposition = predisposition
    if predisposition == "fight":
        stats = ["STR","DEX","CON"]
    if predisposition == "sneak":
        stats = ["STR","DEX","WIS"]
    if predisposition == "cast":
        stats = ["DEX","INT","WIS"]
    if predisposition == "heal":
        stats = ["STR","CON","WIS"]
    
    random_stat = random.choice(stats)
    stat_value = getattr(person,random_stat)
    setattr(person,random_stat,stat_value + 1)

    person.move = person.STR + person.DEX + person.CON
    person.mana = person.INT + person.DEX + person.CHA

    wealth_baseline = random.randint(0,50)
    wealth = 0
    family = random.choice(open('events/family.txt').read().splitlines())
    family_background = f"Your family: {family}.\n"
    person.background += family_background

    if family == "Broken home":
        wealth = wealth_baseline -d(20) / 2
    if family == "Family broke apart gradually":
        wealth = wealth_baseline - d(20)
    if family == "Average family":
        wealth = wealth_baseline
    if family == "Family gradually expanded":
        wealth = wealth_baseline + d(20)
    if family == "Tightknit":
        wealth = wealth_baseline * 2
    person.wealth += wealth

    life_event(person=person,event_file="events/childhood.csv")
    life_event(person=person,event_file="events/childhood.csv")

    wealth_background = "You grew up "
    if wealth < 20:
        wealth_background += "in squalor.\n"
    elif wealth < 50:
        wealth_background += "poor.\n"
    elif wealth < 80:
        wealth_background += "better off than some, not as well off as others.\n"
    elif wealth < 90:
        wealth_background += "well off.\n"
    elif wealth < 100:
        wealth_background += "wealthy.\n"
    else:
        wealth_background += "rich.\n"
    person.background += wealth_background
    
    if wealth > 95:
        person.AC += 8
        person.weapon += 7
    elif wealth > 75:
        person.AC += 6
        person.weapon += 5
    elif wealth > 50:
        person.AC += 4
        person.weapon += 3
    elif wealth > 30:
        person.AC += 2
        person.weapon += 1
    


def life_event(person,event_file):
    event_collection = {}
    with open(event_file, newline="\n", encoding="utf-8") as events:
        all_events = csv.reader(events, delimiter=';')
        for event in all_events:
            event_collection[event[0]] = [event[1],event[2],int(event[3])]

    first_event = event_collection[str(random.randint(1,12))]
    first_event_text = first_event[0] +"\n"
    first_event_stat = first_event[1]
    first_event_value = first_event[2]
    person.background += first_event_text 
    stat_value = getattr(person,first_event_stat)
    setattr(person,first_event_stat,stat_value + first_event_value)    

            

    	







    
        

        

        





if __name__ == "__main__":
    main()