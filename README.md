# Simple Query Service in python (API)
## App Structure
* app: api server code
* bin: start server script
* etc: config file

## Functions
* PyMongo
* CORS
* Page Query

## TODO
* cache

## Example
```
http://127.0.0.1:5000/actors/1/events?page=1
```

```
{
  "next_page": {
    "has_next": true, 
    "next_page_url": "?page_size=1&page=2", 
    "page": 2, 
    "page_size": 1
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
    }
  ]
}
```