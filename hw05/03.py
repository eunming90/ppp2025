fruit_cal = {"hanravong": 50, "strawberry": 34, "banana": 77}
fruit_weight = {}
for fruit in fruit_cal:
    weight = int(input(f"{fruit}의 그람수를 입력하세요: "))
    fruit_weight[fruit] = weight
total_calories = 0
for fruit in fruit_cal:
    fruit_calories = (fruit_cal[fruit] * fruit_weight[fruit]) / 100
    total_calories += fruit_calories
    print(f"{fruit}의 칼로리는 {fruit_calories}kcal입니다.")

print(f"총 칼로리는 {total_calories}kcal입니다.")
