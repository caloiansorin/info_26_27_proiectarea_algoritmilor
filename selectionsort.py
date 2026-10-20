sir = [20, 34, 75, 15, 22, 11, 99, 12]

for i in range(len(sir)-1):
    nrMic = i
    for j in range(i+1, len(sir)):
        if sir[j] < sir[nrMic]:
            nrMic = j            
    sir[i], sir[nrMic] = sir[nrMic], sir[i]

print("Sirul a fost sortat", sir)