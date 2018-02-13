from datetime import date

def filter_list(task_list, task_status='incomplete'):
    if task_status == 'incomplete':
        return filter(lambda task: not task.complete, task_list)
    elif task_status == 'complete':
        return filter(lambda task: task.complete == True, task_list)
    elif task_status == 'today':
        return filter(lambda task: (not task.complete) and task.due <= date.today(), task_list) 


def sort_list(task_list):
    return sorted(task_list, key=lambda task: task.due)


def complete_task(task_list, task_integer):
    filtered_list = filter_list(task_list)
    sorted_list = sort_list(filtered_list)
    print('Completed: {}'.format(sorted_list[task_integer].description))
    sorted_list[task_integer].complete_task()
    task_list = sorted_list[:]
    return task_list


def delete_task(task_list, task_integer):
    filtered_list = filter_list(task_list)
    sorted_list = sort_list(filtered_list)
    deleted = sorted_list.pop(task_integer)
    print('Deleted: {}'.format(deleted.description))
    task_list = sorted_list[:]
    return task_list
