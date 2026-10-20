sir = [17, 3, 19, 122, 11]

n = len(sir)

for i in range(n-1):
    for j in range(n-i-1):
        if sir[j] > sir[j+1]:
            sir[j], sir[j+1] = sir[j+1], sir[j]

print("Sirul a fost sortat", sir)