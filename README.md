# Exercise: implement the journey and todo API

## STEP 1: Check the etc config
* hippo.refresh_data: if true, we can refresh model data at start
* mongo: check mongo URI and db name

## STEP 2: Develop task api (REST)

### STEP 2-1: Implement task model
1. implement app/model/task.py
2. uncomment app/model/__init__.py (from task import TaskModel)

### STEP 2-2: Implement todo api
1. implement app/api/todo.py
2. uncomment app/api/__init__.py (from todo import get_api as get_todo_api)

### STEP 2-3: Using init tasks
* uncomment "init_tasks(models)" in app/conf/index.py

### STEP 2-4: Try todo api using POSTMAN
1. import "test/FlaskService.postman_collection.json" to POSTMAN
2. start api
3. try list, get, create, update, delete


## STEP 3: Develop journey api (Page Query)

### STEP 3-1: Implement event model
1. implement app/model/event.py
2. uncomment app/model/__init__.py (from event import EventModel)

### STEP 3-2: Implement journey api
1. implement app/api/journey.py
2. uncomment app/api/__init__.py (from journey import get_api as get_journey_api)

### STEP 3-3: Using init tasks
* uncomment "init_events(models)" in app/conf/index.py

### STEP 3-4: Try journey api using POSTMAN
1. start api
2. try "list events by actor"
