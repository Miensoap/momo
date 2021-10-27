# #윤년
# print("[윤년 판별 프로그램입니다.]\n[종료는 0 입력]")
# while True:
# 	year = int(input("해를 입력하세요 : "))
# 	if year==0:
# 		print("종료되었습니다.")
# 		break
# 	elif (year%4==0 and year%100 != 0):
# 		print(f"{year}년 ===> 윤년(1번조건)")
# 	elif year%400==0:
# 		print(f"{year}년 ===> 윤년(2번조건)")

# 	else:
# 		print(f"{year}년 ===> 윤년 아님")
# # 30분전
# atime,aminute=input("시간을 입력하세요 : ").split()

# if int(atime)>23 or int(atime)<0 or int(aminute)>59 or int(aminute)<0:
# 	print("잘못된 시간입니다.")
# elif int(aminute) < 30:
# 	bminute=int(aminute)+30
# 	btime=int(atime)-1
# elif  int(aminute)>=30:
# 	bminute=int(aminute)-30
# 	btime=atime

# print(f"현재 시간은 {atime}시 {aminute}분 입니다.")
# print(f"30분전 시간은 {btime}시 {bminute}분 입니다.")


#신조어 퀴즈
class Word():
    def __init__(self, sinzo, show1, show2, ans):
        self.sinzo = sinzo
        self.show1 = show1
        self.show2 = show2
        self.ans = ans

    def show_question(self):
        print(f"{self.sinzo} 의 뜻은?\n1.{self.show1}\n2.{self.show2}")

    def check_answer(self, answer):
        if answer == self.ans:
            print("정답입니다!")
        else:
            print("틀렸습니다!")


def go(q):
    q.show_question()
    q.check_answer(int(input("=>")))


q1 = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
# q1.show_question()
# q1.check_answer(int(input("=>")))
go(q1)
q2 = Word("애빼시", "애교 빼면 시체", "애들은 빼빼로 시시해", 1)
go(q2)
