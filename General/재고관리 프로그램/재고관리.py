import json
import os


class VendingMachine:

  def __init__(self, filename='products.json'):
    self.filename = filename
    self.load_products()

  def load_products(self):
    if os.path.exists(self.filename):
      with open(self.filename, 'r') as file:
        self.products = json.load(file)
    else:
      self.products = {}

  def save_products(self):
    with open(self.filename, 'w') as file:
      json.dump(self.products, file, ensure_ascii=False, indent=4)

  def add_product(self, name, price):
    self.products[name] = price
    self.save_products()
    print(f"제품 '{name}'이(가) 추가되었습니다. 가격: {price}원")

  def delete_product(self, name):
    if name in self.products:
      del self.products[name]
      self.save_products()
      print(f"제품 '{name}'이(가) 삭제되었습니다.")
    else:
      print(f"제품 '{name}'이(가) 존재하지 않습니다.")

  def update_product(self, name):
    if name not in self.products:
      print(f"제품 '{name}'이(가) 존재하지 않습니다.")
      return

    print("수정할 항목을 선택하세요:")
    print("1. 제품 이름")
    print("2. 가격")
    print("3. 제품 이름 및 가격")

    choice = input("선택 (1/2/3): ")

    if choice == '1':
      new_name = input("새로운 제품 이름을 입력하세요: ")
      self.products[new_name] = self.products.pop(name)
      self.save_products()
      print(f"제품 이름이 '{name}'에서 '{new_name}'으로 변경되었습니다.")
    elif choice == '2':
      new_price = int(input("새로운 가격을 입력하세요: "))
      self.products[name] = new_price
      self.save_products()
      print(f"제품 '{name}'의 가격이 {new_price}원으로 변경되었습니다.")
    elif choice == '3':
      new_name = input("새로운 제품 이름을 입력하세요: ")
      new_price = int(input("새로운 가격을 입력하세요: "))
      self.products[new_name] = new_price
      del self.products[name]
      self.save_products()
      print(f"제품 '{name}'이(가) '{new_name}'으로 변경되었고, 가격은 {new_price}원입니다.")
    else:
      print("잘못된 선택입니다.")

  def display_products(self):
    if not self.products:
      print("등록된 제품이 없습니다.")
      return
    print("현재 등록된 제품:")
    for name, price in self.products.items():
      print(f"제품 이름: {name}, 가격: {price}원")


def main():
  vending_machine = VendingMachine()

  while True:
    print("\n재고관리 메뉴:")
    print("1. 제품 추가")
    print("2. 제품 삭제")
    print("3. 제품 수정")
    print("4. 제품 목록 보기")
    print("5. 종료")

    choice = input("선택하세요: ")

    if choice == '1':
      name = input("제품 이름을 입력하세요: ")
      price = int(input("제품 가격을 입력하세요: "))
      vending_machine.add_product(name, price)
    elif choice == '2':
      name = input("삭제할 제품 이름을 입력하세요: ")
      vending_machine.delete_product(name)
    elif choice == '3':
      name = input("수정할 제품 이름을 입력하세요: ")
      vending_machine.update_product(name)
    elif choice == '4':
      vending_machine.display_products()
    elif choice == '5':
      print("프로그램을 종료합니다.")
      break
    else:
      print("잘못된 선택입니다.")


if __name__ == "__main__":
  main()
