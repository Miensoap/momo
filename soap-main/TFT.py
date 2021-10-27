#TFT
wilo = []
gold = 0
win = 0
lose = 0


#연승연패
def gold_streak(win, lose):
    if 4 > win >= 2 or 4 > lose >= 2:
        return 1
    elif win == 4 or lose == 4:
        return 2
    elif win >= 5 or lose >= 7:
        return 3
    else:
        return 0


#이자
def gold_interest(gold):
    if 20 > gold >= 10:
        return 1
    elif 30 > gold >= 20:
        return 2
    elif 40 > gold >= 30:
        return 3
    elif 50 > gold >= 40:
        return 4
    elif gold >= 50:
        return 5
    else:
        return 0


wn = input("라운드 결과 : ")
print(wn)
for i in wn:
    wilo.append(i)
for id in range(len(wilo)):
    # print(id)
    if id % 7 == 3:
        wilo.insert(id, "ch")
    elif id % 7 == 6:
        wilo.insert(id, "cr")

print(wilo)

# a=["a","b","c","d","e"]
# a.insert(3,"adadd")
# print(a)

#골드 계산
for i in wn:
    gold += 5  #기본
    gold_interest(gold)
    #승 : +1원,연승+1,연패 초기화
    if i == "o":
        gold += 1
        win += 1
        lose = 0
        earn = gold_streak(win, lose)
        gold += earn
    #패 : 연승 초기화, 연패+1
    elif i == "x":
        win = 0
        lose += 1
        earn = gold_streak(win, lose)
        gold += earn
    #크립 : 연승/연패 그대로
    elif i == "cr" or "ch":
        earn = gold_streak(win, lose)
        gold += earn

print(f"골드 : {gold}")
