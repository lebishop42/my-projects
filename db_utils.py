import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# GETTING DB VALUES FOR THE API
def get_catalogue():
    catalogue_list = []
    try:
        db_name = 'horses'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB:{db_name}")

        query = """
            SELECT horse_name, age, colour, price
             FROM catalogue
             WHERE status != "sold";"""

        cur.execute(query)

        result = cur.fetchall() #creates tuples

        for item in result:
            dict_item = {"Horse name": item[0],
                         "Age": item[1],
                         "Colour": item[2],
                         "Price": item[3]}
            catalogue_list.append(dict_item)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

        return catalogue_list


# NEW ENTRY FOR SOLD_LIST TABLE
def add_to_sold_list(buyer_name, sold_horse_name):

    try:
        db_name = 'horses'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB:{db_name}")

        query = """
               INSERT INTO sold_list (buyer_name, sold_horse_name)
               VALUES 
               ('{buyer_name}','{sold_horse_name}');""".format(buyer_name=buyer_name, sold_horse_name=sold_horse_name)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# DB CATALOGUE UPDATE WHEN A HORSE HAS SOLD
def update_db(horse_name, status):

    try:
        db_name = 'horses'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB:{db_name}")

        query = """
               UPDATE catalogue 
               SET status = '{status}'
               WHERE horse_name = '{horse_name}';
               """.format(horse_name=horse_name, status=status)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# ADDING A NEW LISTING TO DB CATALOGUE
def listing_to_db(horse_name, age, colour, price, status):

    try:
        db_name = 'horses'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB:{db_name}")

        query = """
               INSERT INTO catalogue (horse_name, age, colour, price, status)
               VALUES 
               ('{horse_name}','{age}', '{colour}', '{price}', '{status}');""".format(horse_name=horse_name, age=age, colour=colour, price=price, status=status)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


