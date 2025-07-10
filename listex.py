# 숫자(점수)를 3개를 input으로 입력
# 숫자는 list(0~2번째 방에 저장)
# 총점 ,평균 구하여 출력

score=[0,0,0]
score[0]=int(input("국어 점수 입력:"))
score[1]=int(input("수학 점수 입력:"))
score[2]=int(input("영어 점수 입력:"))
score=[]
score.append(int(input("국어 점수 입력 :")))
score.append(int(input("수학 점수 입력 :")))
score.append(int(input("영어 점수 입력 :")))

# tot=score[0]+score[1]+score[2]
tot=sum(score)
avg=tot/3 #정수와정수 ->실수 나올수도 있음
print("총점은",tot,"평균은",avg)
