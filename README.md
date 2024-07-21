# HORSE EXCHANGE Programme

## OVERVIEW:

This programme was built to practise making a Flask app which connects a MySQL database to an API, and allows a 'client/customer' to interact with the API with the 'main' programme and make changes to the API and database. 

 The programme allows you to 'buy' or advertise a horse for sale on a catalogue. It takes data about horses for sale from an API (originating from a database). When the user buys or lists a horse for sale, they are asked for details about which horse to buy (or details of one they want to list to sell). This information is relayed to the API and then fed to the database.  
To conclude, the user is shown the changes made to the buying/selling catalogue as a result of their chosen interaction. 

### How the programme should work:
 The user is welcomed and offered a choice of buying or selling a horse.
 If buying, the user is shown a list of available horses (catalogue). There are some horses already sold in the DB catalogue so only the horses available "for sale" are shown to the user. PrettyTable is used to generate a table to present this data attractively.
 The user is asked to input which horse they would like to buy and the user's name.
 These values (user name and horse name) are added onto the API to show the sale made (this information on the API is fed to the DB via the flask app and DB query functions in the db_utils file).
 The chosen horse is also marked as 'sold' by the API and this information is also updated in the DB via the flask app and functions in the db_utils file.
 The user is then shown an updated catalogue with the bought horse removed from it.

 If the buyer opts to sell a horse, they are asked for details of the horse (name, age, colour, price).
 These entries are validated where appropriate and then posted onto the API, along with data for the DB catalogue to show this entry is "for sale".
 Using the flask app, this new listing is also relayed to the DB using the functions in the db_utils file.
 Finally, the user is shown the catalogue with their newly listed horse at the bottom.

## REQUIREMENTS:

* Horses_catalogue.sql (to create underlying database and tables)
* config.py file (details to authenticate the db connection)
* flask-app.py file (creates the flask app, app functions and interacts with functions in db_utils)
* main.py (for the user interaction programme)
* db_utils.py (for connection to database and to allow information to be passed to and from the app to the database)
* __init__.py (to allow Python to treat things in this directory as modules to import from)
* flask Python package (you may need to install if not already installed on device/venv)
* jsonify Python package (see above re installation)
* json Python package (see above re installation)
* requests Python package (see above re installation)
* prettytable Python package (see above re installation)
* mysql.connector Python package (pip install: mysql-connector-python)


## SETTING UP GUIDE:

1. Please see the Requirements above and make sure you have all listed file. You may need to 'pip install' some of
these if not already installed on your device/venv.
2. Open and run the sql file (Horses.sql) in MySQL Workbench so that you have the horses database and tables which
the programme will use and update.
3. Open the config.py file and in the 'PASSWORD' field, please input your password to allow you to connect to MySQL
Workbench where you have run the 'horses' database file.
4. Open the flask_app.py file and the db_utils.py file, ensure that no other programmes are using port 5001 on your device run the 'flask_app' file to
establish the API connection.
5. Once the API connection is made and the app is running, you can open and run the 'main' file which will allow you to buy
and sell on the Horse Exchange as described above.
