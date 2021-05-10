import csv

with open('answer_skt.csv', 'r') as t1, open('submission_skt.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

count = 0
wrong = 0
score = 0.0
for line in filetwo:
    if line not in fileone:  wrong +=1
    count += 1

score = round((count - wrong) / count *100, 3)

print(score)

t1.close()
t2.close()