DemoText = "Я помню чудное мгновенье\n" \
           "Передо мной явилась ты"

def CodeText(S):
    SS = ""
    for i in range(len(S)):
        C = S[i]
        K = ord(C)
        K += 1
        CC = chr(K)
        SS = SS + CC
    return SS