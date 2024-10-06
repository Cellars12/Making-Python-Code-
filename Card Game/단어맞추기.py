import random

def choose_word():
    words = {
        "사과": "빨간색 과일",
        "바나나": "노란색 과일",
        "오렌지": "주황색 과일",
        "포도": "작고 둥글며 보라색 또는 녹색인 과일",
        "키위": "털이 있는 갈색 과일",
        "복숭아": "부드러운 껍질과 달콤한 과일",
        "딸기": "작고 빨간색이며, 씨가 밖에 있는 과일"
    }
    word, hint = random.choice(list(words.items()))
    return word, hint

def display_hangman(tries):
    stages = [  # 단계별 그림
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word, hint = choose_word()
    word_completion = "_" * len(word)  # 숨겨진 단어
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("단어 맞추기 게임에 오신 것을 환영합니다!")
    print(display_hangman(tries))
    print(f"숨겨진 단어: {' '.join(word_completion)}")

    while not guessed and tries > 0:
        guess = input("알파벳이나 단어를 입력하세요, 또는 '힌트'를 입력하세요: ").lower()

        if guess == '힌트':
            print(f"힌트: {hint}")
            continue

        if len(guess) == 1 and guess.isalpha():  # 알파벳 하나 입력
            if guess in guessed_letters:
                print("이미 추측한 알파벳입니다.")
            elif guess not in word:
                print(f"{guess}는 단어에 없습니다.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"잘했어요! {guess}는 단어에 있습니다.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # 단어 전체 입력
            if guess in guessed_words:
                print("이미 추측한 단어입니다.")
            elif guess != word:
                print(f"{guess}는 정답이 아닙니다.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("유효한 입력이 아닙니다.")

        print(display_hangman(tries))
        print(f"숨겨진 단어: {' '.join(word_completion)}")
        print(f"추측한 알파벳: {', '.join(guessed_letters)}")

    if guessed:
        print("축하합니다! 단어를 맞추셨습니다!")
    else:
        print(f"아쉽습니다! 정답은 {word}였습니다.")

    restart = input("다시 하시겠습니까? (y/n): ").lower()
    if restart == 'y':
        play_hangman()
    else:
        print("게임을 종료합니다.")

# 게임 실행
if __name__ == "__main__":
    play_hangman()
