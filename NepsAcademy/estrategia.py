# Estratégia Gulosa

V = int(input())
cem = cinquenta = vintecinco = dez = cinco = um = 0

if V >= 100:
    cem = V // 100
    V = V - (cem * 100)
if V >= 50:
    cinquenta = V // 50
    V = V - (cinquenta * 50)
if V >= 25:
    vintecinco = V // 25
    V = V - (vintecinco * 25)
if V >= 10:
    dez = V // 10
    V = V - (dez * 10)
if V >= 5:
    cinco = V // 5
    V = V - (cinco * 5)
if V >= 1:
    um = V // 1
    V = V - um

total = cem + cinquenta + vintecinco + dez + cinco + um

print(total)
