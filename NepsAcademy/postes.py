#Postes
#https://neps.academy/br/exercise/41

N = int(input())
postes = list(map(int, input().split()))

def subs_reforçs(postes):
    subs = 0
    reforcs = 0
    for poste in postes:
        if poste < 50:
            subs += 1
        if poste >= 50 and poste < 85:
            reforcs += 1

    return subs, reforcs
    
subs, reforcs = subs_reforçs(postes)
print(subs, reforcs)
