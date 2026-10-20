sir = [95, 66, 16, 12, 2, 19, 80, 5]

for i in range(1, len(sir)):
    for j in range(i-1, -1, -1):
        if sir[j] > sir[j+1]:
            sir[j], sir[j+1] = sir[j+1], sir[j]

print("Sirul a fost sortat", sir)