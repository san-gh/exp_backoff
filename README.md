
# exp_backoff
Server with exp back off

### To run server 
```
python3 -m venv env
source ./env/bin/activate
python -m pip install -r requirements.txt
python -m manage.py migrate
uvicorn exp_async.asgi:application --reload
```

### API endpoints 
1. 
```
POST http://127.0.0.1:8000/payments/post/
```

Request:
```
{
    "txnType": "credit",
    "amount":  110
}
```
Response:
```
{
    "id": 25,
    "Txn Type": "credit",
    "Amount ": 110.0,
    "Status": "In Progress"
}
```

2.
```
GET http://127.0.0.1:8000/payments/<txn id>
```
Response
```
{
    "id": 19,
    "Txn Type": "credit",
    "Amount ": 110.0,
    "Status": "Failed"
}
```
