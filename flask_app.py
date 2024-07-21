import json
from flask import Flask, jsonify, request
from db_utils import get_catalogue, add_to_sold_list, listing_to_db, update_db

app = Flask(__name__)


# RETRIEVING THE CATALOGUE FROM DB FOR API
@app.route('/catalogue', methods=['GET'])
def api_catalogue():
    return jsonify(get_catalogue())


# ADDING RECORDS OF SALES TO API
@app.route('/bought_list', methods=['POST'])
def add_to_bought_list():
    sale = request.get_json()
    add_to_sold_list(
        buyer_name=sale['buyer_name'],
        sold_horse_name=sale['sold_horse_name']
    )
    return jsonify(sale)


# UPDATE CATALOGUE (AND DB) CHANGE OF STATUS TO SOLD
@app.route('/catalogue', methods=['PUT'])
def update_sale():
    new_sale = request.get_json()
    update_db(
        horse_name=new_sale['horse_name'],
        status=new_sale['status']
    )
    return jsonify(new_sale)


# ADDING A NEW LISTING TO API (&DB) CATALOGUES
@app.route('/catalogue', methods=['POST'])
def add_api_listing():
    new_listing = request.get_json()
    listing_to_db(
        horse_name=new_listing['horse_name'],
        age=new_listing['age'],
        colour=new_listing['colour'],
        price=new_listing['price'],
        status=new_listing['status']
    )
    return jsonify(new_listing)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

