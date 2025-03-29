def sum_n(n):
    return sum(range(1, n+1))

def main():
    n = int(input("정수를 입력하세요: "))
    result = sum_n(n)
    print(result)

if __name__ == "__main__":
    main()
