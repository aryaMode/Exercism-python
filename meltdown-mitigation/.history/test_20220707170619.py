dice = [5, 1, 5, 1, 5]
freqDic = {}

for index, key in enumerate(dice):
    if key in freqDic:
        index += 1
    freqDic[key] += index

print(freqDic)
