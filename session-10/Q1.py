tasks = {
    101: {'id': 101, 'title': 'Fix login bug', 'assignee': 'Ali', 'priority': 'HIGH', 'status': 'OPEN'},
    102: {'id': 102, 'title': 'Update API', 'assignee': 'Sara', 'priority': 'MEDIUM', 'status': 'IN_PROGRESS'},
    103: {'id': 103, 'title': 'Write tests', 'assignee': 'Ali', 'priority': 'LOW', 'status': 'DONE'},
}
#list meghdar haye mojaz
PRIORITIES = ['LOW', 'MEDIUM', 'HIGH']
STATUSES = ['OPEN', 'IN_PROGRESS', 'DONE']


ALLOWED_MOVES = {
    'OPEN': ['IN_PROGRESS'],
    'IN_PROGRESS': ['DONE'],
    'DONE': [],
}

#tabe ke az karbar shenase migire  fasele haro pak mikone 
def read_id():
    text = input('Task id: ').strip()
    
    #matn ro be adad tabdil mikone 
    try:
        return int(text)
    except ValueError:
        print('Error: id must be a number.')
        return None

#yek darkhast ro hey chap mikone 
def show_task(task):
    print(f'[{task["id"]}] {task["title"]} | {task["assignee"]} | {task["priority"]} | {task["status"]}')


#shenase migire age motabar nabood kharej mishe 
def create_task():
    task_id = read_id()
    if task_id is None:
        return
    
    #shenasaro check mikone age ghablan vojood dasht ghabool nemikone o kharej mishe 
    if task_id in tasks:
        print('Error: this id already exists.')
        return
    
    #onvane o masool o ... migire horoof bozorg mikone ke hame voroodia ghabool shan
    title = input('Title: ').strip()
    assignee = input('Assignee: ').strip()
    priority = input('Priority (LOW/MEDIUM/HIGH): ').strip().upper()
    
    #age olaviat too list nabood khata mide 
    if priority not in PRIORITIES:
        print('Error: invalid priority.')
        return

    #vaziat darkhast jadid hamishe open hast
    tasks[task_id] = {
        'id': task_id,
        'title': title,
        'assignee': assignee,
        'priority': priority,
        'status': 'OPEN',
    }
    print('Task created.')


#darkhast ro ba shenase neshoon mide age nabood payammide not found 
def read_tasks():
    choice = input('1) one task  2) all tasks: ').strip()
    if choice == '1':
        task_id = read_id()
        if task_id is None:
            return
        if task_id in tasks:
            show_task(tasks[task_id])
        else:
            print('Task not found.')
    
    #hame darkhast haro mide yeki yeki chap mikonim
    else:
        if not tasks:
            print('No tasks.')
        for task in tasks.values():
            show_task(task)


#aval check mikonim yeki az 3 vaziat hast ya na 
def change_status(task, new_status):
    if new_status not in STATUSES:
        print('Error: invalid status.')
        return False
    
    
    if new_status not in ALLOWED_MOVES[task['status']]:
        print(f'Error: cannot go from {task["status"]} to {new_status}.')
        return False
    
    #age mojaz bashe vaziat avaz mishe o True barmigardoone
    task['status'] = new_status
    return True


#baraye update o taghir moshakhasate jadid 
def update_task():
    task_id = read_id()
    if task_id is None:
        return
    if task_id not in tasks:
        print('Task not found.')
        return

    task = tasks[task_id]
    print('Leave a field empty to keep the old value.')
    title = input(f'Title ({task["title"]}): ').strip()
    assignee = input(f'Assignee ({task["assignee"]}): ').strip()
    priority = input(f'Priority ({task["priority"]}): ').strip().upper()
    status = input(f'Status ({task["status"]}): ').strip().upper()

    if priority and priority not in PRIORITIES:
        print('Error: invalid priority. Nothing changed.')
        return
    if status and status != task['status']:
        if not change_status(task, status):
            return

    if title:
        task['title'] = title
    if assignee:
        task['assignee'] = assignee
    if priority:
        task['priority'] = priority
    print('Task updated.')


# ---------- Delete ----------
def delete_task():
    task_id = read_id()
    if task_id is None:
        return
    
    #vaghtit nist  khata mide va ba try/except modiriat mikonim khataro
    try:
        task = tasks[task_id]
    except KeyError:
        print('Error: task not found.')
        return
    
    #code faghat ba 'y' edame mide 
    if task['status'] in ('IN_PROGRESS', 'DONE'):
        answer = input(f'Task is {task["status"]}. Are you sure? (y/n): ').strip().lower()
        if answer != 'y':
            print('Delete cancelled.')
            return
    
    #del oon kilid ro pak mikone az dictionary
    del tasks[task_id]
    print('Task deleted.')



def search_tasks():
    
    #karbar moshakhas mikone bar che asasi jostojoo beshe 
    field = input('Search by (assignee/priority/status): ').strip().lower()
    if field not in ('assignee', 'priority', 'status'):
        print('Error: invalid field.')
        return
    value = input('Value: ').strip()


    #moteghayer ke az karbar geretim ro lower mikonim yeki beshan bad barresi mikonim chizi peyda shod ya na 
    found = False
    for task in tasks.values():
        if task[field].lower() == value.lower():
            show_task(task)
            found = True
    if not found:
        print('Nothing found.')



def move_status():
    task_id = read_id()
    if task_id is None:
        return
    if task_id not in tasks:
        print('Task not found.')
        return
    task = tasks[task_id]
    new_status = input(f'New status (now {task["status"]}): ').strip().upper()
    if change_status(task, new_status):
        print('Status changed.')


#gozaresh koli baraye karhaye tamoom shode o baz 
def report():
    total = len(tasks)
    done = 0
    open_count = 0
    for task in tasks.values():
        if task['status'] == 'DONE':
            done += 1
        elif task['status'] == 'OPEN':
            open_count += 1
    print(f'Total: {total} | Done: {done} | Open: {open_count}')


#gozaresh baraye masool
def assignee_report():
    all_count = {}
    open_count = {}
    for task in tasks.values():
        name = task['assignee']
        all_count[name] = all_count.get(name, 0) + 1
        
        #tedad progres open 
        if task['status'] != 'DONE':
            open_count[name] = open_count.get(name, 0) + 1

    for name, count in all_count.items():
        print(f'{name}: {count} tasks, {open_count.get(name, 0)} not done')

    if open_count:
        #dictioanry migarde bishtarin open count ro bar migardoone
        busiest = max(open_count, key=open_count.get)
        print(f'Most open work: {busiest} ({open_count[busiest]})')
    else:
        print('Nobody has open work.')


#shoroo barname
def main():
    actions = {
        '1': create_task,
        '2': read_tasks,
        '3': update_task,
        '4': delete_task,
        '5': search_tasks,
        '6': move_status,
        '7': report,
        '8': assignee_report,
    }
    #loop bi nahayat ke menue ro neshoon mide va ba 0 az menu kharej mishe 
    while True:
        print('\n1) Create 2) Read 3) Update 4) Delete 5) Search '
              '6) Change status 7) Report 8) Assignee report 0) Exit')
        choice = input('Choice: ').strip()
        if choice == '0':
            print('Bye!')
            break
        if choice in actions:
            actions[choice]()
        else:
            print('Invalid choice.')

#barname shoroo mishe 
main()