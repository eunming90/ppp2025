def gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} * {i} = {dan * i}")
def main():
    dan = int(input("구구단을 출력할 숫자를 입력하세요 :"))
    gugudan(dan)
if __name__ == "__main__":
    main()
