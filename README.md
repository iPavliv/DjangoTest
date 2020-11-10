# Test task in Django

## Technologies
* Python (3.9.0)
* Django (3.1.3)
* PostgreSQL 13


## Start app:
Requires installed PostgreSQL and created db `DjangoTest`.
### Routes:
```
/orders-by-period/ - to get information about orders in certain perion of time
/most-purchased/ - to get 20 most sellable articles in certain period of time
```
### Generate records 
Use management command to add to db Order and OrderItem records:
```
python manage.py generate_orders `number of records`
```
