
temp_c = float(input("섭씨 온도를 입력하세요: "))
temp_f = temp_c * 9 / 5 + 32
print("화씨 온도는 {}도 입니다.".format(temp_f))
weight = float(input("몸무게(kg)를 입력하세요: "))
height = float(input("키(m)를 입력하세요: "))
import math
BMI = weight / math.pow(height,2)
print("BMI는 {}입니다.".format(BMI))
radius = float(input("반지름을 입력하세요: "))
circle_area = math.pi *math.pow(radius,2)
print("반지름이 {}인 원의 넓이는 {}입니다.".format(radius,circle_area))
lower = float(input("아랫변을 입력하세요: "))
upper = float(input("윗변을 입력하세요: "))
height = float(input("높이를 입력하세요: "))
trapezoid_area = (lower + upper) * height / 2
print("아랫변이 {}, 윗변이 {}, 높이가 {}인 사다리꼴의 넓이는 {}입니다.".format(lower,upper,height,trapezoid_area))
hanravong = int(input("한라봉의 그람수를 입력하세요"))
strawberry = int(input("딸기의 그람수를 입력하세요"))
banana = int(input("바나나의 그람수를 입력하세요"))
hanravong_cal = (hanravong/100)*50
strawberry_cal = (strawberry/100)*34
banana_cal = (banana/100)*77
print("한라봉의 칼로리는 {}kcal입니다.".format(hanravong_cal))
print("딸기의 칼로리는 {}kcal입니다.".format(strawberry_cal))
print("바나나의 칼로리는 {}kcal입니다.".format(banana_cal))
x1 = int(input("x1을 입력하세요: "))
y1 = int(input("y1을 입력하세요: "))
x2 = int(input("x2을 입력하세요: "))
y2 = int(input("y2을 입력하세요: "))
distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print("두 점 사이의 거리는 {}입니다.".format(distance))
