import math
weight = float(input("몸무게(kg)를 입력하세요"))
height = float(input("키(m)를 입력하세요"))
BMI = weight / math.pow(height,2)
print( BMI)
if 23 <= BMI <= 24.9 :
    print("{}는 비만 전 단계입니다.".format(BMI))
if 25 <= BMI <= 29.9 :
    print("{}는 1단계 비만입니다.".format(BMI))
if 30<= BMI <= 34.9 :
    print("{}는 2단계 비만입니다.".format(BMI))
if 35<= BMI  :
    print("{}는 3단계 비만입니다.".format(BMI))

x = int(input("x좌표를 입력하세요"))
y = int(input("y좌표를 입력하세요"))
if x > 0 and y > 0 :
    print("1사분면에 있습니다.")
if x < 0 and y > 0 :
    print("2사분면에 있습니다.")
if x < 0 and y< 0:
    print("3사분면에 있습니다.")
if x>0 and y <0:
    print("4사분면에 있습니다.")
    
fruit_cal = {"hanravong":50, "strawberry":34, "banana":77}
fruit_weight = {"hanravong":int(input("한라봉의 그람수를 입력하세요")), 
                "strawberry":int(input("딸기의 그람수를 입력하세요")),
                "banana":int(input("바나나의 그람수를 입력하세요"))}
hanravong_cal = (fruit_cal["hanravong"] * fruit_weight["hanravong"]) / 100
strawberry_cal = (fruit_cal["strawberry"] * fruit_weight["strawberry"]) / 100
banana_cal = (fruit_cal["banana"] * fruit_weight["banana"]) / 100
print(f"한라봉의 칼로리는 {hanravong_cal}kcal입니다.")
print(f"딸기의 칼로리는 {strawberry_cal}kcal입니다.")
print(f"바나나의 칼로리는 {banana_cal}kcal입니다.")  
import math
radius = float(input("반지름을 입력하세요"))
circle_area = math.pi * math.pow(radius,2)
circumference = 2 * math.pi * radius
print(f"반지름이 {radius}인 원의 넓이는 {circle_area:.2f}입니다.")
print(f"반지름이 {radius}인 원의 둘레는 {circumference:.1f}입니다.")