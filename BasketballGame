import tkinter as tk
from tkinter import messagebox
import threading
import time

class BasketballGame:
    def __init__(self, team_a, team_b, duration):
        self.scores = {team_a: 0, team_b: 0}
        self.history = []
        self.start_time = None
        self.is_running = False
        self.duration = duration

    def start_game(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            threading.Thread(target=self.auto_end_game).start()

    def auto_end_game(self):
        time.sleep(self.duration)
        self.end_game()

    def score_point(self, team, points):
        if team in self.scores and points > 0:
            self.scores[team] += points
            self.history.append((team, points))
        else:
            raise ValueError("잘못된 팀 이름이거나 점수는 0보다 커야 합니다.")

    def end_game(self):
        if self.is_running:
            self.is_running = False
            return self.get_score(), self.history
        return None, None

    def get_score(self):
        return self.scores

    def reset_game(self):
        self.scores = {team: 0 for team in self.scores}
        self.history.clear()

    def get_remaining_time(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            remaining_time = max(0, self.duration - elapsed_time)
            return remaining_time
        return 0

class BasketballGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("농구 점수 카운터")

        self.team_a = tk.StringVar()
        self.team_b = tk.StringVar()
        self.duration = tk.IntVar()

        tk.Label(root, text="팀 A 이름:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.team_a).grid(row=0, column=1)

        tk.Label(root, text="팀 B 이름:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.team_b).grid(row=1, column=1)

        tk.Label(root, text="게임 지속 시간(초):").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.duration).grid(row=2, column=1)

        tk.Button(root, text="게임 시작", command=self.start_game).grid(row=3, columnspan=2)

        tk.Label(root, text="점수를 추가할 팀:").grid(row=4, column=0)
        self.team_input = tk.StringVar()
        tk.Entry(root, textvariable=self.team_input).grid(row=4, column=1)

        tk.Label(root, text="점수:").grid(row=5, column=0)
        self.points_input = tk.IntVar()
        tk.Entry(root, textvariable=self.points_input).grid(row=5, column=1)

        tk.Button(root, text="점수 추가", command=self.add_score).grid(row=6, columnspan=2)
        tk.Button(root, text="게임 리셋", command=self.reset_game).grid(row=7, columnspan=2)

        self.score_frame = tk.Frame(root)
        self.score_frame.grid(row=8, columnspan=2)
        self.score_label = tk.Label(self.score_frame, text="")
        self.score_label.pack()

        self.time_label = tk.Label(root, text="")
        self.time_label.grid(row=9, columnspan=2)

    def start_game(self):
        team_a_name = self.team_a.get()
        team_b_name = self.team_b.get()
        game_duration = self.duration.get()

        if not team_a_name or not team_b_name or game_duration <= 0:
            messagebox.showwarning("경고", "모든 필드를 올바르게 입력해 주세요.")
            return

        self.game = BasketballGame(team_a_name, team_b_name, game_duration)
        self.game.start_game()
        self.update_score()

    def update_score(self):
        if self.game.is_running:
            score = self.game.get_score()
            self.score_label.config(text=f"현재 점수: {score}")

            remaining_time = self.game.get_remaining_time()
            self.time_label.config(text=f"남은 시간: {int(remaining_time)}초")

            self.root.after(1000, self.update_score)
        else:
            final_scores, history = self.game.end_game()
            if final_scores:
                messagebox.showinfo("게임 종료", f"최종 점수: {final_scores}")
                history_str = "\n".join([f"{team}: {points}점" for team, points in history])
                messagebox.showinfo("점수 기록", f"게임 기록:\n{history_str}")

    def add_score(self):
        team = self.team_input.get()
        points = self.points_input.get()

        if self.game.is_running:
            try:
                self.game.score_point(team, points)
                self.update_score()
            except ValueError as e:
                messagebox.showwarning("경고", str(e))
        else:
            messagebox.showwarning("경고", "게임이 진행 중이 아닙니다.")

    def reset_game(self):
        self.game.reset_game()
        self.score_label.config(text="")
        self.time_label.config(text="")
        self.team_a.set("")
        self.team_b.set("")
        self.duration.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = BasketballGUI(root)
    root.mainloop()
