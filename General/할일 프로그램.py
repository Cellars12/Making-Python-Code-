import json
import os
from datetime import datetime, timedelta
import shutil

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
        self.settings = self.load_settings()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def load_settings(self):
        if os.path.exists('settings.json'):
            with open('settings.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        return {'default_priority': '2', 'reminder_period': 1}

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def save_settings(self):
        with open('settings.json', 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, ensure_ascii=False, indent=4)

    def add_task(self, task, due_date, priority=None, category='', tags=None):
        if priority is None:
            priority = self.settings['default_priority']
        self.tasks.append({
            'task': task,
            'due_date': due_date,
            'completed': False,
            'priority': priority,
            'category': category,
            'tags': tags or []
        })
        self.save_tasks()
        print(f'할 일 추가됨: {task}, 기한: {due_date}, 우선순위: {priority}, 카테고리: {category}, 태그: {tags}')

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed = self.tasks.pop(task_index)
            self.save_tasks()
            print(f'할 일 제거됨: {removed["task"]}')
        else:
            print('잘못된 할 일 인덱스입니다.')

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print(f'할 일이 완료됨: {self.tasks[task_index]["task"]}')
        else:
            print('잘못된 할 일 인덱스입니다.')

    def edit_task(self, task_index, new_task, new_due_date, new_priority, new_category, new_tags):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].update({
                'task': new_task,
                'due_date': new_due_date,
                'priority': new_priority,
                'category': new_category,
                'tags': new_tags
            })
            self.save_tasks()
            print(f'할 일이 수정됨: {new_task}, 기한: {new_due_date}, 우선순위: {new_priority}, 카테고리: {new_category}, 태그: {new_tags}')
        else:
            print('잘못된 할 일 인덱스입니다.')

    def show_tasks(self, filter_type=None):
        filtered_tasks = self.tasks
        if filter_type == 'completed':
            filtered_tasks = [task for task in self.tasks if task['completed']]
        elif filter_type == 'overdue':
            filtered_tasks = [task for task in self.tasks if datetime.strptime(task['due_date'], '%Y-%m-%d') < datetime.now() and not task['completed']]
        elif filter_type == 'pending':
            filtered_tasks = [task for task in self.tasks if not task['completed']]
        elif filter_type == 'high':
            filtered_tasks = [task for task in self.tasks if task['priority'] == '1']
        elif filter_type == 'medium':
            filtered_tasks = [task for task in self.tasks if task['priority'] == '2']
        elif filter_type == 'low':
            filtered_tasks = [task for task in self.tasks if task['priority'] == '3']

        if not filtered_tasks:
            print('할 일이 없습니다.')
        else:
            print('당신의 할 일:')
            for index, task_info in enumerate(filtered_tasks):
                status = '✔️' if task_info['completed'] else '❌'
                overdue = datetime.strptime(task_info['due_date'], '%Y-%m-%d') < datetime.now() and not task_info['completed']
                highlight = '⚠️' if overdue else ''
                tags = ', '.join(task_info['tags']) if task_info['tags'] else '태그 없음'
                print(f'{index}: [{status}] {task_info["task"]} (기한: {task_info["due_date"]}, 우선순위: {task_info["priority"]}, 카테고리: {task_info["category"]}, 태그: {tags}) {highlight}')

    def export_tasks(self):
        with open('todo_list.txt', 'w', encoding='utf-8') as file:
            for task_info in self.tasks:
                status = '✔️' if task_info['completed'] else '❌'
                tags = ', '.join(task_info['tags']) if task_info['tags'] else '태그 없음'
                file.write(f'[{status}] {task_info["task"]} (기한: {task_info["due_date"]}, 우선순위: {task_info["priority"]}, 카테고리: {task_info["category"]}, 태그: {tags})\n')
        print('할 일 목록이 todo_list.txt로 내보내졌습니다.')

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if keyword.lower() in task['task'].lower()]
        if not found_tasks:
            print('일치하는 할 일이 없습니다.')
        else:
            print('일치하는 할 일:')
            for index, task_info in enumerate(found_tasks):
                status = '✔️' if task_info['completed'] else '❌'
                print(f'{index}: [{status}] {task_info["task"]} (기한: {task_info["due_date"]}, 우선순위: {task_info["priority"]}, 카테고리: {task_info["category"]}, 태그: {task_info["tags"]})')

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: (x['completed'], x['priority']))
        self.save_tasks()
        print('할 일이 완료 상태와 우선순위에 따라 정렬되었습니다.')

    def backup_tasks(self):
        backup_file = f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        shutil.copy(self.filename, backup_file)
        print(f'백업 생성됨: {backup_file}')

    def group_by_category(self):
        categories = {}
        for task in self.tasks:
            category = task['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(task)

        for category, tasks in categories.items():
            print(f'\n카테고리: {category}')
            for index, task_info in enumerate(tasks):
                status = '✔️' if task_info['completed'] else '❌'
                print(f'  {index}: [{status}] {task_info["task"]} (기한: {task_info["due_date"]}, 우선순위: {task_info["priority"]})')

    def statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        pending_tasks = total_tasks - completed_tasks
        print(f'전체 할 일: {total_tasks}, 완료된 할 일: {completed_tasks}, 미완료된 할 일: {pending_tasks}')

    def show_tasks_within_period(self, days):
        cutoff_date = datetime.now() + timedelta(days=days)
        filtered_tasks = [task for task in self.tasks if datetime.strptime(task['due_date'], '%Y-%m-%d') <= cutoff_date]

        if not filtered_tasks:
            print('이 기간 내에 할 일이 없습니다.')
        else:
            print(f'다음 {days}일 내에 기한이 만료되는 할 일:')
            for index, task_info in enumerate(filtered_tasks):
                status = '✔️' if task_info['completed'] else '❌'
                print(f'  {index}: [{status}] {task_info["task"]} (기한: {task_info["due_date"]}, 우선순위: {task_info["priority"]}, 카테고리: {task_info["category"]})')

    def priority_statistics(self):
        priority_count = {'1': 0, '2': 0, '3': 0}
        for task in self.tasks:
            priority_count[task['priority']] += 1

        print('우선순위 통계:')
        print(f'높음 (1): {priority_count["1"]}, 중간 (2): {priority_count["2"]}, 낮음 (3): {priority_count["3"]}')

    def set_user_settings(self, default_priority=None, reminder_period=None):
        if default_priority:
            self.settings['default_priority'] = default_priority
        if reminder_period:
            self.settings['reminder_period'] = reminder_period
        self.save_settings()
        print('사용자 설정이 업데이트되었습니다.')

    def check_reminders(self):
        for task in self.tasks:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
            if not task['completed'] and due_date <= datetime.now() + timedelta(days=self.settings['reminder_period']):
                print(f'알림: 할 일 "{task["task"]}"의 기한이 {task["due_date"]}입니다.')

def main():
    todo_list = ToDoList()
    while True:
        print('\n1. 할 일 추가')
        print('2. 할 일 제거')
        print('3. 할 일 완료')
        print('4. 할 일 수정')
        print('5. 할 일 목록 보기')
        print('6. 할 일 내보내기')
        print('7. 할 일 검색')
        print('8. 할 일 정렬')
        print('9. 할 일 백업')
        print('10. 카테고리별 그룹화')
        print('11. 통계')
        print('12. 기간 내 할 일 보기')
        print('13. 우선순위 통계')
        print('14. 사용자 설정')
        print('15. 알림 확인')
        print('16. 종료')

        choice = input('옵션을 선택하세요: ')

        try:
            if choice == '1':
                task = input('할 일을 입력하세요: ')
                due_date = input('기한 입력 (YYYY-MM-DD): ')
                priority = input('우선순위 입력 (1-높음, 2-중간, 3-낮음) 또는 기본값 사용 시 비워두기: ')
                category = input('카테고리 입력: ')
                tags = input('태그 입력 (쉼표로 구분): ').split(',') if input('태그 추가할까요? (y/n): ').lower() == 'y' else []
                todo_list.add_task(task, due_date, priority or None, category, tags)
            elif choice == '2':
                todo_list.show_tasks()
                task_index = int(input('제거할 할 일 인덱스를 입력하세요: '))
                todo_list.remove_task(task_index)
            elif choice == '3':
                todo_list.show_tasks()
                task_index = int(input('완료할 할 일 인덱스를 입력하세요: '))
                todo_list.complete_task(task_index)
            elif choice == '4':
                todo_list.show_tasks()
                task_index = int(input('수정할 할 일 인덱스를 입력하세요: '))
                new_task = input('새로운 할 일 입력: ')
                new_due_date = input('새로운 기한 입력 (YYYY-MM-DD): ')
                new_priority = input('새로운 우선순위 입력 (1-높음, 2-중간, 3-낮음): ')
                new_category = input('새로운 카테고리 입력: ')
                new_tags = input('새로운 태그 입력 (쉼표로 구분): ').split(',')
                todo_list.edit_task(task_index, new_task, new_due_date, new_priority, new_category, new_tags)
            elif choice == '5':
                filter_type = input('필터 (모두, 완료됨, 기한 초과, 미완료, 높음, 중간, 낮음): ').strip().lower()
                todo_list.show_tasks(filter_type if filter_type in ['completed', 'overdue', 'pending', 'high', 'medium', 'low'] else None)
            elif choice == '6':
                todo_list.export_tasks()
            elif choice == '7':
                keyword = input('검색할 키워드를 입력하세요: ')
                todo_list.search_tasks(keyword)
            elif choice == '8':
                todo_list.sort_tasks()
            elif choice == '9':
                todo_list.backup_tasks()
            elif choice == '10':
                todo_list.group_by_category()
            elif choice == '11':
                todo_list.statistics()
            elif choice == '12':
                days = int(input('일수를 입력하세요: '))
                todo_list.show_tasks_within_period(days)
            elif choice == '13':
                todo_list.priority_statistics()
            elif choice == '14':
                default_priority = input('기본 우선순위 입력 (1-높음, 2-중간, 3-낮음) 또는 비워두기: ')
                reminder_period = input('알림 주기 (일수) 입력 또는 비워두기: ')
                todo_list.set_user_settings(default_priority or None, int(reminder_period) if reminder_period.isdigit() else None)
            elif choice == '15':
                todo_list.check_reminders()
            elif choice == '16':
                print('종료합니다...')
                break
            else:
                print('잘못된 선택입니다. 다시 시도하세요.')
        except ValueError:
            print('잘못된 입력입니다. 숫자를 입력하세요.')
        except Exception as e:
            print(f'오류 발생: {e}')

if __name__ == '__main__':
    main()
