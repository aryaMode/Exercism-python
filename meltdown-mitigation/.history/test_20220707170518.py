freqDic = {}    
    
for index, key in enumerate(dice):
    if key in freqDic:
        index+=1
freqDic[key] = index