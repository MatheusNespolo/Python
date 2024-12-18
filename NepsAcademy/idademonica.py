#A Idade de Dona Mônica

idadesFilhos = []
idadeDM = int(input())
idadesFilhos.append(int(input()))
idadesFilhos.append(int(input()))
idadeFilho3 = idadeDM - sum(idadesFilhos)
idadesFilhos.append(idadeFilho3)

print(max(idadesFilhos))
