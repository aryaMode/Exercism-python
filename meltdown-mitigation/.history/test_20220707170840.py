dice = [5, 1, 5, 1, 5]
freqDic = {}

for index, key in enumerate(dice):
    if key in freqDic:
        freqDic[key] += 1
    freqDic[key] = 0

print(freqDic)
