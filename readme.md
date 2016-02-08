####1) Setup

```
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

####2) Check if the database (here, cars) exists

`$ psql cars`

####3) If so, drop the database

`$ dropdb cars`

####4) Then create the database

```
$ createdb cars
$ psql cars < database.sql
```

####5) Make sure the Flask app is connected to the cars database in model.py

`app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'`

####6) Because the database has table data written from database.sql, no need to create tables in Flask; if not, make sure to run the .createall() once:

`db.createall()`