# Score categories.
# Change the values as you see fit.
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


def score(dice, category):

    freqDic = {}
    threeExists, twoExists = False, False
    total = 0
    for index, key in enumerate(dice):
        index = int(index)
        key = int(key)

        if key in freqDic:
            freqDic[key] = int(freqDic[key])+1
            continue

        freqDic[key] = 1
    if (2 in freqDic) and (3 in freqDic) and (4 in freqDic) and (5 in freqDic) and (6 in freqDic):
        BIG_STRAIGHT = 30
    if (1 in freqDic) and (2 in freqDic) and (3 in freqDic) and (4 in freqDic) and (5 in freqDic):
        LITTLE_STRAIGHT = 30
    for key, value in freqDic.items():
        total += key * value
        if value == 2:
            twoExists = True
        if value == 3:
            threeExists = True
       # CHOICE += int(key)
        if value == 5:
            YACHT = 50
        if value == 4:
            FOUR_OF_A_KIND = int(key) * 4
        if key == 1:
            ONES = 1 * value

        if key == 2:
            TWOS = 2 * value

        if key == 3:
            THREES = 3 * value

        if key == 4:
            FOURS = 4 * value

        if key == 5:
            FIVES = 5 * value

        if key == 6:
            SIXES = 6 * value
    if twoExists and threeExists:
        FULL_HOUSE = total

    if category == "YACHT":
        return YACHT
    if category == "ONES":
        return ONES
    if category == "TWOS":
        return TWOS
    if category == "THREES":
        return THREES
    if category == "FOURS":
        return FOURS
    if category == "FIVES":
        return FIVES
    if category == "SIXES":
        return SIXES
    if category == "FULL_HOUSE":
        return FULL_HOUSE
    if category == "FOUR_OF_A_KIND":
        return FOUR_OF_A_KIND
    if category == "LITTLE_STRAIGHT":
        return LITTLE_STRAIGHT
    if category == "BIG_STRAIGHT":
        return BIG_STRAIGHT
    if category == "CHOICE":
        return CHOICE


print(score([2, 3, 4, 5, 6], "B_STRAIGHT"))
