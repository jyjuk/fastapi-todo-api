tasks = []
task_id_counter = 1


def get_all_tasks():
    return tasks


def create_task(data):
    global task_id_counter
    task = {
        "id": task_id_counter,
        "title": data.title,
        "completed": data.completed
    }
    tasks.append(task)
    task_id_counter += 1
    return task


def update_task(task_id, data):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.title
            task["completed"] = data.completed
            return task
    return None


def delete_task(task_id):
    global tasks
    before = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == before:
        return False
    return True
