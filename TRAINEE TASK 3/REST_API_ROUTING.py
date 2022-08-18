from ast import Suite
from sqlite3 import connect
from turtle import title
from unittest import result
from flask import Flask, jsonify, request
import accounts_controller
from TASK3_DB_GEN import create_db
app = Flask(__name__)
#ALL GET ROUTES
@app.route('/finduser', methods =["GET"])
def get_account():
    ID = request.args['id']
    account = accounts_controller.get_account_details(ID)
    return jsonify(account)

@app.route('/finduserposts', methods =["GET"])
def get_account_posts():
    ID = request.args['id']
    account = accounts_controller.get_account_posts(ID)
    return jsonify(account)

@app.route('/findpost', methods =["GET"])
def get_post():
    ID = request.args['id']
    account = accounts_controller.get_post(ID)
    return jsonify(account)
    
@app.route('/findpostcomments', methods =["GET"])
def get_post_comments():
    ID = request.args['id']
    account = accounts_controller.get_post_comments(ID)
    return jsonify(account)

@app.route('/findcomment')
def get__comment():
    ID = request.args['id']
    account = accounts_controller.get_comment(ID)
    return jsonify(account)
#FIND TOTAL ROUTES
@app.route('/findtotalusers', methods =["GET"])
def get_total_accounts():
    account = accounts_controller.get_total_users()
    return jsonify(account)

@app.route('/findtotalposts', methods =["GET"])
def get_total_posts():
    account = accounts_controller.get_total_posts()
    return jsonify(account)

@app.route('/findtotalcomments', methods = ["GET"])
def get_total_comments():
    account = accounts_controller.get_total_comments()
    return jsonify(account)
#ALL ADD ROUTINGS
@app.route("/adduser", methods = ["POST"])
def insert_user():
    user_details = request.get_json()
    ID = accounts_controller.get_next_user()
    Name = user_details ["Name"]
    Username = user_details ["Username"]
    Email = user_details ["Email"]
    Street = user_details ["Street"]
    Suite = user_details ["Suite"]
    City = user_details ["City"]
    Zipcode = user_details ["Zipcode"]
    LAT = user_details ["LAT"]
    LON = user_details ["LON"]
    Phone = user_details ["Phone"]
    Website = user_details ["Website"]
    CompanyName = user_details ["CompanyName"]
    CompanyCP = user_details ["CompanyCP"]
    CompanyBS = user_details ["CompanyBS"]
    result = accounts_controller.add_user (ID , Name , Username , Email , Street , Suite , City , Zipcode , LAT , LON , Phone , Website , CompanyName , CompanyCP , CompanyBS)
    return jsonify(result)

@app.route("/addpost", methods = ["POST"])
def insert_account():
    post_details = request.get_json()
    Title = post_details["Title"]
    ID = accounts_controller.get_next_post()
    UserID = post_details ["UserID"]
    Body = post_details ["Body"]

    result = accounts_controller.add_post (Title, ID, UserID, Body)
    return jsonify(result)

@app.route("/addcomment", methods = ["POST"])
def insert_comment():
    comment_details = request.get_json()
    PostID = comment_details["PostID"]
    ID = accounts_controller.get_next_comment()
    Name = comment_details["Name"]
    Email = comment_details["Email"]
    Body = comment_details["Body"]
    result = accounts_controller.add_comment (PostID, ID, Name, Email, Body)
    return jsonify(result)


@app.route ("/account/deleteuser", methods = ["DELETE"])
def delete_account():
    ID = request.args['id']
    result = accounts_controller.delete_account(ID)
    return jsonify(result)

@app.route ("/deletepost", methods = ["DELETE"])
def delete_post():
    ID = request.args['id']
    result = accounts_controller.delete_post(ID)
    return jsonify(result)

@app.route ("/deletecomment", methods = ["DELETE"])
def delete_comment():
    ID = request.args['id']
    result = accounts_controller.delete_comment(ID)
    return jsonify(result)

@app.route ("/deleteuserposts", methods = ["DELETE"])
def delete_accountposts():
    ID = request.args['id']
    result = accounts_controller.delete_account_posts(ID)
    return jsonify(result)

@app.route ("/deletepostcomments", methods = ["DELETE"])
def delete_postcomments():
    ID = request.args['id']
    result = accounts_controller.delete_post_comments(ID)
    return jsonify(result)

if __name__ == "__main__":
        create_db()


app.run(host='0.0.0.0', port=8000, debug=False)
    




