from os import listdir
from os.path import isfile, isdir, join, exists
from typing import Callable, List, Tuple
from testing import TestError


def get_all_tests(test_dir: str) -> List[Tuple[str, str]]:
    tests = []
    for entry in listdir(test_dir):
        entry_path = join(test_dir, entry)
        if isfile(entry_path):
            with open(entry_path, 'r', encoding='utf-8') as file:
                tests.append((entry.split('.')[0], file.read()))
    return sorted(tests)


def test_on_test(test: str, run_test: Callable, solution_module):
    try:
        run_test(test, solution_module)
        return "\033[1;92mOK\033[00m"
    except TestError as e:
        return f"\033[1;91mFailed: {e}\033[00m"
    except Exception as e:
        return f"\033[1;91mUnknown exception: {e}\033[00m"


def test_task(task_name: str):
    tests = get_all_tests(join('tasks', task_name, 'tests'))
    run_test = getattr(getattr(getattr(__import__(f'tasks.{task_name}.checker'), task_name), 'checker'), 'run_test')
    solution_module = getattr(__import__(f'solutions.{task_name}'), task_name)
    for test_name, test in tests:
        print(f"\033[96m┃ {test_name}\033[00m - {test_on_test(test, run_test, solution_module)}")


def get_all_tasks() -> List[str]:
    return [f for f in listdir('tasks') if isdir(join('tasks', f))]


def test():
    print("\033[1;94mTesting started ...\033[00m")
    for task in get_all_tasks():
        if exists(join('solutions', f"{task}.py")):
            print("\033[96m---------------------------\033[00m")
            print(f"\033[93mTask: {task} ...\033[00m")
            test_task(task)
            print("\033[96m---------------------------\033[00m")
    print("\033[1;94mTesting successfully completed\033[00m")


if __name__ == "__main__":
    test()