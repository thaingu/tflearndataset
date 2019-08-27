import string


lines = []
translator = str.maketrans('', '', string.punctuation)


with open('amazon_baby_reviews.txt') as inputfile:
    lines = [line.rstrip('\n').translate(translator) for line in inputfile]

while("" in lines):
    lines.remove("")

with open('amazon_baby_reviews_punct.txt', 'w') as f:
    for item in lines:
        f.write("%s\n" % item)

with open('trainX.txt', 'w') as f:
    for item in lines[0:10000]:
        f.write("%s\n" % item)

with open('testX.txt', 'w') as f:
    for item in lines[10000:20000]:
        f.write("%s\n" % item)

with open('amazon_baby_binary.txt') as inputfile:
    nums = [line.rstrip('\n').translate(translator) for line in inputfile]

with open('trainY.txt', 'w') as f:
    for item in nums[0:10000]:
        f.write("%s\n" % item)

with open('testY.txt', 'w') as f:
    for item in nums[10000:20000]:
        f.write("%s\n" % item)
