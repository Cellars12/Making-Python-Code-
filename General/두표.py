import json

vote_topic = "가장 좋아하는 프로그래밍 언어는?"
vote_options = ["Python", "Java", "C++", "JavaScript", "Ruby"]
vote_count = {option: 0 for option in vote_options}
voters = set()  # 중복 투표 방지

def display_options():
    print(f"\n주제: {vote_topic}")
    for i, option in enumerate(vote_options, start=1):
        print(f"{i}. {option}")

def cast_vote():
    name = input("이름을 입력하세요 (투표 인증): ")
    if name in voters:
        print("이미 투표하셨습니다.")
        return
    
    while True:
        try:
            choice = int(input("투표할 번호를 입력하세요: "))
            if 1 <= choice <= len(vote_options):
                selected_option = vote_options[choice - 1]
                vote_count[selected_option] += 1
                voters.add(name)  # 사용자 추가
                print(f"{selected_option}에 투표하셨습니다!")
                break
            else:
                print("잘못된 번호입니다. 다시 시도하세요.")
        except ValueError:
            print("숫자를 입력해야 합니다. 다시 시도하세요.")

def display_results():
    print("\n투표 결과:")
    for option, count in vote_count.items():
        print(f"{option}: {count}표")

def save_results():
    with open("vote_results.json", "w") as f:
        json.dump(vote_count, f)

if __name__ == "__main__":
    while True:
        display_options()
        cast_vote()
        
        another_vote = input("다시 투표하시겠습니까? (y/n): ")
        if another_vote.lower() != 'y':
            break

    display_results()
    save_results()
    print("투표가 종료되었습니다. 결과가 'vote_results.json'에 저장되었습니다.")
