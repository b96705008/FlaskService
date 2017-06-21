# Simple Query Service in python (API)
## App Structure
* app: api server code
* bin: start server script
* etc: config file

## Functions
* PyMongo
* CORS
* Cache
* Page Query

## How to start?
```
./bin/run.sh [cfg name or default]
```

## Example

### Simple query
```
http://127.0.0.1:5000/actors/1/events?page_size=2&page=1
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
