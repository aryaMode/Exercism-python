dice = [5, 1, 5, 1, 5]
freqDic = {}

for index, key in enumerate(dice):
    index = int(index)
    key = int(key)

    if key in freqDic:
        freqDic[key] = int(freqDic[key])+1

    freqDic[key] = 0

print(freqDic)
