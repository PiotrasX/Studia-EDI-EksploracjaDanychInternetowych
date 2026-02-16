rawData = open("SMSSpamCollection.tsv", encoding="UTF-8").read()

parsedData = rawData.replace('\t', '\n').split('\n')
labelList = parsedData[0::2]
textList = parsedData[1::2]

print("Długość labelList: ", len(labelList))
print("Długość textList: ", len(textList))

if len(labelList) > len(textList):
    labelList = labelList[:-(len(labelList) - len(textList))]
elif len(textList) > len(labelList):
    textList = textList[:-(len(textList) - len(labelList))]

print("\nDługość labelList: ", len(labelList))
print("Długość textList: ", len(textList))
