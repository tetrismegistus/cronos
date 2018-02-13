from serialization import save_file, load_file
from task import Task, RecurrentTask


FILENAME = 'tasks.p'


def test_save(tl):
    save_file(FILENAME, tl)


def test_load():
    return load_file(FILENAME)


task_list = test_load()

for task in task_list:
    print(task.description, task.due)
    try:
        print(task.get_status())
    except AttributeError as e:
        pass
