#지뢰
mine = {
    "M14":
    "\n112.2g\n9~15kg압력\n접촉지점상해 폭풍형 대인지뢰\n1)외관확인\n2)적송마개 제거후 공이 미격발 확인\n3)S->A(다시안돌림!!)\n4)안전크립 제거 공이확인/재결합\n5)기폭제 결합\n6)매설공 굴토(압력판지면)\n7)2/3 일부매설\n8)안전크립 제거\n9)완전매설 위장",
    "M16":
    "\n3/6~9kg압력/n공중도약식 파편형 대인지뢰(0.6~2.4m)\n1)외관확인\n2)휴즈검사대에서 압력두부 360도 회전확인\n3)제1안전핀, 내부멈치핀 제거 공이확인\n4)제2안전핀 상하유격확인, 제거후 공이확인, 재결합\n5)휴즈결합\n6)매설공굴토(압력뿔하단지면)\n7)일부매설\n8)제1안전핀, 내부멈치핀 제거\n9)완전매설 제2안전핀 제거(후 추가위장 금지)",
    "M15":
    "\n1)외관확인/n2)장전플러그분리\n3)S->A C형고리 중앙위치확인, A->S\n4)휴즈 외관확인 안전크립제거 휴즈삽입공에 넣고 안전플러그 결합\n5)매설공굴토 45도 일부매설\n6)S->A\n7)완전매설, 2cm복토",
    "M19":
    "\n1)외관, 안전크립확인\n2)안전크립 제거 S->A 공이 중앙위치 확인, A->S 안전크립 결합\n3)기폭제 결합 후 압력판 결합\n4)매설공굴토 45도\n5)안전크립 제거 S->A\n6)2cm 복토"
}
#지혈법
#심폐소생술
#도수운반법
dosu = {"어깨법": "ㅇㅇ", "부축법": "ㄴㄴ", "받들기법": "ss", "업기법": "ㅇㅇㄹ", "업치기법": "ㅇㅁㅇ"}

print("목록 : 지뢰, 심폐소생술, 도수운반법, 지혈법")
on1 = True
on2 = True
while on1:
    ip1 = input("\n무엇을 보여드릴까요?\n (종료는 x입력)\n")

    if ip1 == "지뢰":
        while on2:
            print("목록 : ", end="")
            for key in mine.keys():
                print(key, end=" ")
                ip2 = input("\n무엇을 보여드릴까요?\n (종료는 x입력)\n")
                if ip2 in mine:
                    for i in mine:
                        if ip2 == i:
                            print(mine[i])
                        elif ip2 == "x":
                            on2 = False
                        else:
                            print("목록에 없습니다.")
        else:
            continue

    elif ip1 == "도수운반법":
        while on2:
            print("목록 : ", end="")
            for key in dosu.keys():
                print(key, end=" ")
            ip3 = input("\n무엇을 보여드릴까요?\n (종료는 x입력)\n")
            if ip3 in dosu:
                for i in dosu:
                    if ip3 == i:
                        print(dosu[i])
                    elif ip3 == "x":
                        on2 = False
            else:
                print("목록에 없습니다.")
    elif ip1 == "x":
        on1 = False
    else:
        print("목록에 없습니다.")
