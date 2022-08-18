import sqlite3
import requests
def get_db():
    conn = sqlite3.connect("accounts.db", isolation_level=None)
    cursor = conn.cursor()
    return conn, cursor
def create_db():
    conn, cursor = get_db()
    cursor.execute("DROP TABLE IF EXISTS posts;")
    cursor.execute("CREATE TABLE IF NOT EXISTS posts (Title TEXT, ID INTEGER PRIMARY KEY, UserID INTEGER, Body TEXT)")
    cursor.execute("DROP TABLE IF EXISTS comments;")
    cursor.execute("CREATE TABLE IF NOT EXISTS comments (PostID INTEGER, ID INTEGER PRIMARY KEY, Name TEXT, Email TEXT, Body TEXT)")
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY, Name TEXT, Username TEXT, Email TEXT, Street TEXT, Suite TEXT, City TEXT, Zipcode TEXT, LAT TEXT, LON TEXT, Phone TEXT, Website TEXT, CompanyName TEXT, CompanyCP TEXT, CompanyBS TEXT)")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    fetch = response.json()
    url2 = "https://jsonplaceholder.typicode.com/users"
    response2 = requests.get(url2)
    fetch2 = response2.json()
    url3 = "https://jsonplaceholder.typicode.com/comments"
    response3 = requests.get(url3)
    fetch3 = response3.json()

    for i in range(len(fetch)):
        fetchuser = fetch [i] ["userId"]
        fetchID = fetch [i] ["id"]
        fetchtitle = fetch [i] ["title"]
        fetchbody = fetch [i] ["body"]
        cursor.execute("INSERT INTO posts(Title, ID, UserID, Body) VALUES ((?), (?), (?), (?))",(fetchtitle, fetchID, fetchuser, fetchbody))
        conn.commit()
    for i in range(len(fetch2)):
        fetchID = fetch2 [i] ["id"]
        fetchname = fetch2 [i] ["name"]
        fetchusername = fetch2 [i] ["username"]
        fetchemail = fetch2 [i] ["email"]
        fetchstreet = fetch2 [i] ["address"]["street"]
        fetchsuite = fetch2 [i] ["address"]["suite"]
        fetchcity = fetch2 [i] ["address"]["city"]
        fetchzip = fetch2 [i] ["address"]["zipcode"]
        fetchlat = fetch2 [i] ["address"]["geo"]["lat"]
        fetchlong = fetch2 [i]["address"]["geo"]["lng"]
        fetchphone = fetch2 [i] ["phone"]
        fetchwebsite = fetch2 [i] ["website"]
        fetchcompanyname = fetch2 [i] ["company"]["name"]
        fetchcompanycp = fetch2 [i] ["company"]["catchPhrase"]
        fetchcompanybs = fetch2 [i] ["company"]["bs"] 
        cursor.execute("INSERT INTO users(ID , Name , Username , Email , Street , Suite , City , Zipcode , LAT , LON , Phone , Website , CompanyName , CompanyCP , CompanyBS) VALUES ((?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?))",(fetchID, fetchname,fetchusername,fetchemail,fetchstreet,fetchsuite,fetchcity,fetchzip,fetchlat,fetchlong,fetchphone,fetchwebsite,fetchcompanyname,fetchcompanycp,fetchcompanybs))
        conn.commit()
    for i in range(len(fetch3)):
        fetchpostID = fetch3 [i] ["postId"]
        fetchID = fetch3 [i] ["id"]
        fetchname = fetch3 [i] ["name"]
        fetchemail = fetch3 [i] ["email"]
        fetchbody = fetch3 [i] ["body"]
        cursor.execute("INSERT INTO comments(PostID, ID, Name, Email, Body) VALUES ((?), (?), (?), (?), (?))",(fetchpostID, fetchID, fetchname, fetchemail, fetchbody))
        conn.commit()

create_db()