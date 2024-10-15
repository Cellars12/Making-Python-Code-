import os
import json

def initialize_file():
    """Management.txt 파일이 존재하지 않을 경우 초기화합니다."""
    if not os.path.isfile("Management.txt"):
        with open("Management.txt", "w", encoding="utf-8") as File:
            temp1 = {
                "First_Name": [],
                "Last_Name": [],
                "Phone_num": [],
                "Room_Type": [],
                "Days": [],
                "Price": [],
                "Room": [],
            }
            json.dump(temp1, File)

def load_data():
    """Management.txt에서 데이터를 로드합니다."""
    with open("Management.txt", "r", encoding="utf-8") as File:
        return json.load(File)

def save_data(data):
    """Management.txt에 데이터를 저장합니다."""
    with open("Management.txt", "w", encoding="utf-8") as File:
        json.dump(data, File)

def menu():
    options = {
        1: {"title": "새 고객 정보 추가", "method": add},
        2: {"title": "기존 고객 정보 수정", "method": modify},
        3: {"title": "고객 정보 검색", "method": search},
        4: {"title": "모든 고객 정보 보기", "method": view},
        5: {"title": "고객 정보 삭제", "method": remove},
        6: {"title": "프로그램 종료", "method": exit_program},
    }

    print(f"\n\n{' '*25}호텔 데이터베이스 관리 소프트웨어에 오신 것을 환영합니다\n\n")

    for num, option in options.items():
        print(f"{num}: {option['title']}")
    print()

    try:
        choice = int(input("선택지를 입력하세요 (1-6): "))
        options[choice]['method']()
    except (ValueError, KeyError):
        print("잘못된 선택입니다. 다시 시도하세요.")
        menu()

def add():
    data = load_data()
    
    first_name = input("\n이름을 입력하세요: ")
    last_name = input("\n성씨를 입력하세요: ")
    phone_num = input("\n전화번호를 입력하세요 (+91 제외): ")

    print("현재 이용 가능한 방은 다음과 같습니다:")
    print("1 - 일반 (500/일)")
    print("2 - 디럭스 (1000/일)")
    print("3 - 슈퍼 디럭스 (1500/일)")
    print("4 - 프리미엄 디럭스 (2000/일)")

    try:
        room_type = int(input("\n어떤 방을 원하십니까 (1-4): "))
        prices = {1: 500, 2: 1000, 3: 1500, 4: 2000}
        room_names = {1: "일반", 2: "디럭스", 3: "슈퍼 디럭스", 4: "프리미엄 디럭스"}
        
        if room_type not in prices:
            raise ValueError("잘못된 방 유형입니다.")

        x = prices[room_type]
        room_name = room_names[room_type]

    except ValueError:
        print("방 유형 입력이 잘못되었습니다. 다시 시도하세요.")
        return add()

    days = int(input("몇 일 머무실 건가요: "))
    total_cost = x * days
    print(f"\n지불하실 금액: {total_cost}")
    
    payment = input("결제 방법 (카드/현금/온라인): ").capitalize()
    if payment not in ["카드", "현금", "온라인"]:
        print("잘못된 결제 방법입니다. 다시 시도하세요.")
        return add()

    room_num = str(int(max(data["Room"], default="500")) + 1)

    print(f"부여된 방 번호: {room_num}")
    print(f"이름: {first_name} {last_name}")
    print(f"전화번호: +91{phone_num}")
    print(f"방 유형: {room_name}")
    print(f"숙박 일수: {days}")

    data["First_Name"].append(first_name)
    data["Last_Name"].append(last_name)
    data["Phone_num"].append(phone_num)
    data["Room_Type"].append(room_name)
    data["Days"].append(days)
    data["Price"].append(total_cost)
    data["Room"].append(room_num)

    save_data(data)
    print("\n고객 정보가 성공적으로 데이터베이스에 추가되었습니다.")
    exit_menu()

def modify():
    data = load_data()
    
    if not data["Room"]:
        print("\n데이터베이스에 데이터가 없습니다.\n")
        menu()
    
    room_num = input("\n방 번호를 입력하세요: ")

    if room_num not in data["Room"]:
        print("방 번호를 찾을 수 없습니다.")
        return modify()

    index = data["Room"].index(room_num)

    print("\n1 - 이름 변경")
    print("2 - 성 변경")
    print("3 - 전화번호 변경")

    try:
        choice = int(input("\n선택지를 입력하세요: "))
        
        if choice == 1:
            category = "First_Name"
        elif choice == 2:
            category = "Last_Name"
        elif choice == 3:
            category = "Phone_num"
        else:
            print("잘못된 선택입니다.")
            return modify()

        new_value = input(f"새로운 {category.replace('_', ' ')}를 입력하세요: ")
        data[category][index] = new_value

        save_data(data)
        print("\n고객 정보가 성공적으로 업데이트되었습니다.")
        exit_menu()

    except ValueError:
        print("잘못된 입력입니다. 다시 시도하세요.")
        return modify()

def search():
    data = load_data()
    
    if not data["Room"]:
        print("\n데이터베이스에 데이터가 없습니다.\n")
        menu()
    
    room_num = input("\n방 번호를 입력하세요: ")

    if room_num in data["Room"]:
        index = data["Room"].index(room_num)
        print(f"\n이름: {data['First_Name'][index]}")
        print(f"성: {data['Last_Name'][index]}")
        print(f"전화번호: {data['Phone_num'][index]}")
        print(f"방 유형: {data['Room_Type'][index]}")
        print(f"숙박 일수: {data['Days'][index]}")
        print(f"지불 금액: {data['Price'][index]}")
        print(f"방 번호: {data['Room'][index]}")
    else:
        print("방 번호를 찾을 수 없습니다.")
    
    exit_menu()

def remove():
    data = load_data()
    
    if not data["Room"]:
        print("\n데이터베이스에 데이터가 없습니다.\n")
        menu()
    
    room_num = input("\n방 번호를 입력하세요: ")

    if room_num in data["Room"]:
        index = data["Room"].index(room_num)
        for key in data:
            del data[key][index]

        save_data(data)
        print("고객 정보가 성공적으로 삭제되었습니다.")
    else:
        print("방 번호를 찾을 수 없습니다.")
    
    exit_menu()

def view():
    data = load_data()
    
    if not data["Room"]:
        print("\n데이터베이스에 데이터가 없습니다.\n")
        menu()

    for index in range(len(data["Room"])):
        print("")
        print("이름:", data["First_Name"][index])
        print("성:", data["Last_Name"][index])
        print("전화번호:", data["Phone_num"][index])
        print("방 유형:", data["Room_Type"][index])
        print("숙박 일수:", data["Days"][index])
        print("지불 금액:", data["Price"][index])
        print("방 번호:", data["Room"][index])
        print("")

    exit_menu()

def exit_program():
    print("")
    print("                             방문해 주셔서 감사합니다")
    print("                                 안녕히 가세요")

def exit_menu():
    print("프로그램을 종료하거나 메인 메뉴로 돌아가시겠습니까?")
    print("1 - 메인 메뉴")
    print("2 - 종료")

    try:
        choice = int(input("선택지를 입력하세요: "))
        if choice == 2:
            exit_program()
        elif choice == 1:
            menu()
        else:
            print("잘못된 선택입니다. 메인 메뉴로 돌아갑니다.")
            menu()
    except ValueError:
        print("잘못된 입력입니다. 메인 메뉴로 돌아갑니다.")
        menu()

# 파일 초기화 및 메뉴 시작
initialize_file()
try:
    menu()
except KeyboardInterrupt:
    print("\n종료 중...")

