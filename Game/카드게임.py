import random


class MemoryGame:

    def __init__(self):
        self.cards = []
        self.max_pairs = 5
        self.chances = 3

    def setup_game(self):
        numbers = list(range(1, self.max_pairs + 1)) * 2  # 숫자 쌍 생성
        random.shuffle(numbers)  # 카드 섞기
        self.cards = numbers

    def display_cards(self, revealed):
        print("카드 상태:")
        for index, card in enumerate(self.cards):
            if revealed[index]:
                print(f"[{card}]", end=' ')
            else:
                print("[*]", end=' ')
        print()

    def play(self):
        self.setup_game()
        revealed = [False] * (self.max_pairs * 2)
        pairs_found = 0

        while pairs_found < self.max_pairs and self.chances > 0:
            self.display_cards(revealed)
            print(f"남은 기회: {self.chances}")
            first_choice = int(input("첫 번째 카드를 선택하세요 (0-9): "))
            second_choice = int(input("두 번째 카드를 선택하세요 (0-9): "))

            if first_choice < 0 or first_choice >= len(
                    self.cards) or second_choice < 0 or second_choice >= len(
                        self.cards):
                print("잘못된 선택입니다. 다시 시도하세요.")
                continue

            if first_choice == second_choice:
                print("같은 카드를 선택할 수 없습니다.")
                continue

            revealed[first_choice] = True
            revealed[second_choice] = True
            self.display_cards(revealed)

            if self.cards[first_choice] == self.cards[second_choice]:
                print("짝을 찾았습니다!")
                pairs_found += 1
            else:
                print("틀렸습니다.")
                revealed[first_choice] = False
                revealed[second_choice] = False
                self.chances -= 1

        if pairs_found == self.max_pairs:
            print("축하합니다! 모든 짝을 찾았습니다!")
        else:
            print("게임이 끝났습니다. 기회를 다 사용하셨습니다.")


if __name__ == "__main__":
    game = MemoryGame()
    game.play()
