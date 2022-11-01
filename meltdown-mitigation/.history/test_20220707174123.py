dice = [5, 1, 2, 1, 5]
freqDic = {}

for index, key in enumerate(dice):
    index = int(index)
    key = int(key)

    if key in freqDic:
        freqDic[key] = int(freqDic[key])+1
        continue

    freqDic[key] = 1
two, three = False, False
print(two, three)
# print(list(freqDic))

YACHT = 0
    ONES = 0
    TWOS = 0
    THREES = 0
    FOURS = 0
    FIVES = 0
    SIXES = 0
    FULL_HOUSE = 0
    FOUR_OF_A_KIND = 0
    LITTLE_STRAIGHT = 0
    BIG_STRAIGHT = 0
    CHOICE = 0
