import random

class Tower:
    def __init__(self, name, damage, range, special_effect=None):
        self.name = name
        self.damage = damage
        self.range = range
        self.level = 1
        self.cost = 50
        self.special_effect = special_effect

    def upgrade(self):
        self.level += 1
        self.damage += 5
        self.cost += 20
        print(f"{self.name}이(가) 업그레이드되었습니다! 현재 데미지: {self.damage}, 비용: {self.cost}")

    def use_special(self, enemies):
        if self.special_effect:
            self.special_effect(enemies)

class Enemy:
    def __init__(self, health, enemy_type, speed, defense=0, level=1):
        self.health = health
        self.type = enemy_type
        self.speed = speed
        self.defense = defense
        self.level = level

    def level_up(self):
        self.level += 1
        self.health += 10  # 레벨업 시 체력 증가
        self.speed += 1    # 레벨업 시 속도 증가
        print(f"{self.type}이(가) 레벨업했습니다! 현재 레벨: {self.level}, 체력: {self.health}, 속도: {self.speed}")

class Game:
    def __init__(self):
        self.towers = []
        self.enemies = []
        self.rounds = 5
        self.score = 0
        self.resources = 100
        self.special_ability_used = False

    def setup_towers(self):
        def explode_effect(enemies):
            for enemy in enemies:
                enemy.health -= 10
                print(f"{enemy.type}이(가) 폭발에 의해 10의 피해를 받았습니다. 남은 체력: {enemy.health}")

        tower_types = [
            Tower("기본 타워", damage=10, range=3),
            Tower("폭발 타워", damage=15, range=1, special_effect=explode_effect),
            Tower("슬로우 타워", damage=5, range=5, special_effect=lambda enemies: self.slow_effect(enemies)),
        ]
        print("타워 종류:")
        for i, tower in enumerate(tower_types):
            print(f"{i + 1}. {tower.name} (데미지: {tower.damage}, 범위: {tower.range}, 비용: {tower.cost})")

        while True:
            num_towers = int(input("몇 개의 타워를 배치할까요? (최소 1개): "))
            if num_towers > 0 and num_towers * tower_types[0].cost <= self.resources:
                break
            else:
                print("자원이 부족하거나 잘못된 입력입니다.")

        for _ in range(num_towers):
            choice = int(input("타워 번호를 선택하세요: ")) - 1
            self.towers.append(tower_types[choice])
            self.resources -= tower_types[choice].cost

    def slow_effect(self, enemies):
        for enemy in enemies:
            if enemy.health > 0:
                enemy.speed = max(1, enemy.speed - 1)
                print(f"{enemy.type}의 속도가 감소했습니다. 현재 속도: {enemy.speed}")

    def spawn_enemies(self, round_number):
        enemy_types = ["슬라임", "고블린", "좀비", "보스"]
        enemy_count = round_number + 2
        self.enemies = []

        for _ in range(enemy_count):
            if random.random() < 0.1 and round_number % 2 == 0:
                self.enemies.append(Enemy(health=100, enemy_type="보스", speed=1))
            else:
                enemy = Enemy(health=random.randint(20, 50), enemy_type=random.choice(enemy_types), speed=random.randint(1, 3))
                self.enemies.append(enemy)

        print(f"\n라운드 {round_number}: {enemy_count}명의 적이 출현했습니다!")

    def attack_enemies(self):
        for tower in self.towers:
            for enemy in self.enemies:
                if enemy.health > 0:
                    damage_dealt = max(tower.damage - enemy.defense, 0)
                    enemy.health -= damage_dealt
                    print(f"{tower.name}이(가) {enemy.type}에게 {damage_dealt}의 피해를 입혔습니다. 남은 체력: {enemy.health}")
                    if enemy.health <= 0:
                        print(f"{enemy.type}이(가) 처치되었습니다!")
                        self.score += 10
                        if random.random() < 0.5:  # 적 처치 시 자원 획득 확률
                            resource_gain = random.randint(5, 15)
                            self.resources += resource_gain
                            print(f"자원을 {resource_gain} 얻었습니다! 현재 자원: {self.resources}")
                        break

    def upgrade_tower(self):
        print("업그레이드할 타워를 선택하세요:")
        for i, tower in enumerate(self.towers):
            print(f"{i + 1}. {tower.name} (레벨: {tower.level}, 데미지: {tower.damage}, 비용: {tower.cost})")

        choice = int(input("타워 번호를 선택하세요: ")) - 1
        if 0 <= choice < len(self.towers):
            if self.resources >= self.towers[choice].cost:
                self.resources -= self.towers[choice].cost
                self.towers[choice].upgrade()
            else:
                print("자원이 부족합니다.")

    def run_game(self):
        self.setup_towers()

        for round_number in range(1, self.rounds + 1):
            self.spawn_enemies(round_number)
            self.attack_enemies()

            # 적 레벨업 (임의로)
            for enemy in self.enemies:
                if random.random() < 0.3:  # 30% 확률로 레벨업
                    enemy.level_up()

            if self.enemies:
                self.upgrade_tower()

        print(f"게임이 종료되었습니다. 최종 점수: {self.score}, 남은 자원: {self.resources}")

if __name__ == "__main__":
    game = Game()
    game.run_game()
