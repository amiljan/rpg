from character import d

def dmg_tester(number):

    normal_roll = 0
    advantage_roll = 0
    disadvantage_roll = 0

    for i in range(number):
        normal_hit = d(20)
        hit1 = d(20)
        hit2 = d(20)
        hits = [hit1,hit2]
        advantage = sorted(hits)[1]
        disadvantage = sorted(hits)[0]

        normal_roll += normal_hit
        advantage_roll += advantage
        disadvantage_roll += disadvantage
    
    print(normal_roll/number)
    print(advantage_roll/number)
    print(disadvantage_roll/number)



for i in range(50):
    dmg_tester(100000)
    print("")
        





