import Demo08U as D8
S = D8.DemoText
S = D8.CodeText(S)

with open("Demo08.cod", mode='w', encoding="utf-8") as F:
    F.write(S)
with open("Demo08.cod", mode='r', encoding="utf-8") as F:
    S = F.read()

S = D8.DecodeText(S)

print(S)