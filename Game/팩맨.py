import random

# 게임 맵
WIDTH, HEIGHT = 10, 10
PACMAN = 'P'
FOOD = '.'
WALL = '#'
EMPTY = ' '

# 게임 상태
class Game:
    def __init__(self):
        self.board = self.create_board()
        self.pacman_pos = (0, 0)
        self.food_pos = self.place_food()
        self.score = 0

    def create_board(self):
        board = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if random.random() < 0.2:  # 20% 확률로 벽 생성
                    board[i][j] = WALL
        board[0][0] = PACMAN  # 팩맨 시작 위치
        return board

    def place_food(self):
        while True:
            food_pos = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
            if self.board[food_pos[0]][food_pos[1]] == EMPTY:
                self.board[food_pos[0]][food_pos[1]] = FOOD
                return food_pos

    def draw_board(self):
        for row in self.board:
            print(' '.join(row))
        print(f"Score: {self.score}")

    def move_pacman(self, direction):
        x, y = self.pacman_pos
        new_pos = {
            'w': (x - 1, y),  # 위
            's': (x + 1, y),  # 아래
            'a': (x, y - 1),  # 왼쪽
            'd': (x, y + 1)   # 오른쪽
        }.get(direction)

        if new_pos:
            if self.is_valid_move(new_pos):
                self.update_position(new_pos)
            else:
                print("Game Over! You hit a wall.")
                return False  # 게임 종료 신호
        return True  # 게임 계속 진행

    def is_valid_move(self, pos):
        x, y = pos
        return 0 <= x < HEIGHT and 0 <= y < WIDTH and self.board[x][y] != WALL

    def update_position(self, new_pos):
        x, y = self.pacman_pos
        self.board[x][y] = EMPTY  # 현재 위치 비우기
        self.pacman_pos = new_pos
        x, y = new_pos
        self.board[x][y] = PACMAN  # 새 위치에 팩맨 배치

        # 음식 먹기
        if new_pos == self.food_pos:
            self.score += 1
            self.food_pos = self.place_food()  # 새로운 음식 배치

# 게임 실행
def main():
    game = Game()
    while True:
        game.draw_board()
        move = input("Move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            if not game.move_pacman(move):
                break  # 게임 종료
        else:
            print("Invalid move! Use 'w', 'a', 's', or 'd'.")

if __name__ == "__main__":
    main()
