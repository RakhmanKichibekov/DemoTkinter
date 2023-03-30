import Demo08U as D8
S = D8.DemoText
print(S)
SS = D8.CodeText(S)

with open("Demo08.cod", mode='w', encoding="utf-8") as F:
    F.write(SS)

S = ""

with open("Demo08.cod", mode='r', encoding="utf-8") as F:
    S = F.read()

print(S)