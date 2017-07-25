# API app using Flask and MongoDB
## Structure
* app: api server code
* bin: start server script
* etc: config file
* sbin: entry app python file

### app folder
* app/conf: flask app initial setting (cache, mongo, auth...)
* app/model: model which connect to MongoDB (or others)
* app/api: flask blueprint route and controller
* app/utils: model, page query related lib

## Functions
* PyMongo
* CORS
* Cache (local or redis)
* Auth
* Page Query

### TODO
* Process async message using Kafka

## How to start?

1. Set this app folder root path
```
export SERVICE_NAME=${PWD}
```

2. Start app with config
```
./bin/run.sh [cfg name or default.cfg]
```

## REST Example (todo API)

### List tasks
```
GET http://localhost:5000/todo/tasks
```
* response
```
{
    "tasks": [
        {
            "_id": "59702b54c412980aaa5aad91",
            "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
            "done": false,
            "title": "Buy groceries"
        },
        {
            "_id": "59702b54c412980aaa5aad92",
            "description": "Need to find a good Python tutorial on the web",
            "done": false,
            "title": "Learn Python"
        }
    ]
}
```

### Get task by id
```
GET http://localhost:5000/todo/tasks/59702b54c412980aaa5aad91
```
* response
```
{
    "task": {
        "_id": "59702b54c412980aaa5aad91",
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": false,
        "title": "Buy groceries"
    }
}
```

### Create task
```
POST http://localhost:5000/todo/tasks
```
* body
```
{
    "title": "Love story",
    "description": "So great!",
    "done": false,
    "xxxx": "XXXXX"
}
```
* response
```
{
    "task": {
        "_id": "59702bbdc412980aaa5aad93",
        "description": "So great!",
        "done": false,
        "title": "Love story"
    }
}
```

### Update task by id
```
PUT http://localhost:5000/todo/tasks/59702bbdc412980aaa5aad93
```
* body
```
{
    "description": "Wow!",
    "done": true,
    "title": "Spark!",
    "error": "will not be updated"
}
```
* response
```
{
    "task": {
        "_id": "59702bbdc412980aaa5aad93",
        "description": "Wow!",
        "done": true,
        "title": "Spark!"
    }
}
```

### Delete task by id
```
DELETE http://localhost:5000/todo/tasks/59702bbdc412980aaa5aad93
```
* response
```
{
    "is_success": true
}
```

## Page Query Example (journey API)

### Simple query
```
http://127.0.0.1:5000/journey/actors/1/events?page_size=2&page=1
```

```
{
  "next_page": {
    "has_next": true,
    "page": 2,
    "page_size": 2
  },
  "result": [
    {
      "_id": "594885e4994aa607c71983b8",
      "action": {
        "time": 5.0,
        "type": "love"
      },
      "actor": {
        "id": "1",
        "type": "customer_id"
      }
    },
    {
      "_id": "594885d1994aa607c71983b7",
      "action": {
        "time": 4.0,
        "type": "love"
      },
      "actor": {
        "id": "1",
        "type": "customer_id"
      }
    }
  ]
}
```

### String equal query
```
http://localhost:5000/journey/actors/1/events?_page_size=2&_page=1&action.type=play
```

```
{
  "next_page": {
    "has_next": false
  },
  "result": [
    {
      "_id": "59488592994aa607c71983b6",
      "action": {
        "time": 3.0,
        "type": "play"
      },
      "actor": {
        "id": "1",
        "type": "customer_id"
      }
    }
  ]
}
```

### String in multiple values query
```
http://localhost:5000/journey/actors/1/events?_page_size=5&_page=1&action.type=play,love
```

```
{
  "next_page": {
    "has_next": false
  },
  "result": [
    {
      "_id": "594885e4994aa607c71983b8",
      "action": {
        "time": 5.0,
        "type": "love"
      },
      "actor": {
        "id": "1",
        "type": "customer_id"
      }
    },
    {
      "_id": "594885d1994aa607c71983b7",
      "action": {
        "time": 4.0,
        "type": "love"
      },
      "actor": {
        "id": "1",
        "type": "customer_id"
      }
    },
    {
      "_id": "59488592994aa607c71983b6",
      "action": {
        "time": 3.0,
        "type": "play"
      },
      "actor": {
        "id": "1",
        "type": "customer_id"
      }
    }
  ]
}
```
