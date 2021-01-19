# tento program ma za ulohu zistit, ci je mozne zostrojit trojuholnik s danymi stranami

strana_a = int(input("strana a v cm = " ))
strana_b = int(input("strana b v cm = " ))
strana_c = int(input("strana c v cm = " ))

if strana_a + strana_b > strana_c:
    print("trojuholnik je mozne zostrojit!")
else:
    print("trojuholnik nie je mozne zostrojit!")