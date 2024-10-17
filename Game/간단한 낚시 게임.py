import random

def 낚시_게임():
    print("=== 🎣 낚시 게임 ===")
    print("좋은 낚시터에 도착했습니다! 물고기를 잡아보세요. 🐟\n")

    총_점수 = 0
    시도_횟수 = 5  # 낚시 시도 횟수

    for i in range(시도_횟수):
        input(f"{i + 1}번째 낚시를 위해 낚시대를 던지려면 Enter를 누르세요... 🌊")
        물고기_크기 = random.randint(1, 20)  # 1부터 20 사이의 랜덤한 물고기 크기
        print(f"🎉 잡은 물고기의 크기: {물고기_크기}cm\n")
        총_점수 += 물고기_크기

    print("🎊 낚시가 끝났습니다! 🎊")
    print(f"🌟 총 점수: {총_점수}cm입니다. 🌟")

낚시_게임()
