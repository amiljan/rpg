from character import d

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