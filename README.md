<pre> <code> ```json { "name": "example-project", "version": "1.0.0", "dependencies": { "express": "^4.18.2" } } ``` </code> </pre>

# Python and AWS test answers

## quiz
It contains theory questions with answers in txt file

## app
There is updated version of problem_solving.py

## lambda
There are functions used in lambdas.
getUser for GET
createUser for POST

Api Gateway URL: https://bzxyrojo0m.execute-api.eu-west-1.amazonaws.com/dev/users

### GET
example request:  
GET https://bzxyrojo0m.execute-api.eu-west-1.amazonaws.com/dev/users?user_id=c8c62d42-c3ec-4fb6-80c4-f5a325917ccd

Response:
```json
{
    "user_id": "c8c62d42-c3ec-4fb6-80c4-f5a325917ccd",
    "first_name": "Richard",
    "age": "23"
}
```

### POST
Example request:  
POST https://bzxyrojo0m.execute-api.eu-west-1.amazonaws.com/dev/users  
Body:
```json
{
  "first_name": "David",
  "age": 24
}
```
Response:
```json
{
    "user_id": "17535575-f1ad-445c-ae8e-317ddce4bd0e"
}
```
