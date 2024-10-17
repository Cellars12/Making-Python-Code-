class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "오류: 0으로 나눌 수 없습니다."
        return a / b

    def run(self):
        print("간단한 계산기")
        while True:
            print("\n옵션:")
            print("1. 덧셈")
            print("2. 뺄셈")
            print("3. 곱셈")
            print("4. 나눗셈")
            print("5. 종료")

            choice = input("옵션을 선택하세요: ")

            if choice in ['1', '2', '3', '4']:
                a = float(input("첫 번째 숫자를 입력하세요: "))
                b = float(input("두 번째 숫자를 입력하세요: "))

                if choice == '1':
                    result = self.add(a, b)
                    print(f"결과: {result}")
                elif choice == '2':
                    result = self.subtract(a, b)
                    print(f"결과: {result}")
                elif choice == '3':
                    result = self.multiply(a, b)
                    print(f"결과: {result}")
                elif choice == '4':
                    result = self.divide(a, b)
                    print(f"결과: {result}")
            elif choice == '5':
                print("계산기를 종료합니다...")
                break
            else:
                print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
