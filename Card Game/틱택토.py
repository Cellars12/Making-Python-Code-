def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # 가로, 세로, 대각선 체크
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # 가로
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # 세로
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # 대각선
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # 대각선
    return None

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    turns = 0

    while True:
        print_board(board)
        print(f"플레이어 {current_player}의 차례입니다.")

        while True:
            try:
                row = int(input("행 번호(0-2)를 입력하세요: "))
                col = int(input("열 번호(0-2)를 입력하세요: "))
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    turns += 1
                    break
                else:
                    print("이미 선택된 자리입니다. 다시 선택하세요.")
            except (ValueError, IndexError):
                print("잘못된 입력입니다. 0, 1, 2 중 하나를 입력하세요.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"플레이어 {winner}가 이겼습니다!")
            break

        if turns == 9:
            print_board(board)
            print("무승부입니다!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    restart = input("다시 하시겠습니까? (y/n): ").lower()
    if restart == 'y':
        play_tic_tac_toe()
    else:
        print("게임을 종료합니다.")

# 게임 실행
if __name__ == "__main__":
    play_tic_tac_toe()
