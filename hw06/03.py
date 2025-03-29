def c2f(t_c):
    return (t_c * 9/5) + 32

def main():
    t_c = float(input("온도를 입력하세요:"))
    t_f = c2f(t_c)
    print(f"{t_c}는 {t_f}입니다.")

if __name__ == "__main__":
    main()
