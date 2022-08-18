from TASK3_DB_GEN import get_db
#ALL GET REQUEST FUNCTIONS
def get_account_details (ID):
    db, cur = get_db()
    statement = "SELECT * FROM users WHERE ID = ?"
    cur.execute(statement, [ID])
    return cur.fetchone()

def get_account_posts (ID):
    db, cur = get_db()
    statement = "SELECT * FROM posts WHERE UserID = ?"
    cur.execute(statement, [ID])
    return cur.fetchall()

def get_post (ID):
    db, cur = get_db()
    statement = "SELECT * FROM posts WHERE ID = ?"
    cur.execute(statement,[ID])
    return cur.fetchone()

def get_post_comments (ID):
    db, cur = get_db()
    statement = "SELECT * FROM comments WHERE PostID = ?"
    cur.execute(statement, [ID])
    return cur.fetchall()

def get_comment (ID):
    db, cur = get_db()
    statement = " SELECT * FROM comments WHERE ID = ?"
    cur.execute(statement, [ID])
    return cur.fetchone()

# GET TOTAL REQUEST FUNCTIONS

def get_total_users():
    db, cur = get_db()
    statement = "SELECT COUNT (*) FROM users"
    cur.execute(statement)
    return int(cur.fetchone()[0])

def get_total_posts():
    db, cur = get_db()
    statement = "SELECT COUNT (*) FROM posts"
    cur.execute(statement)
    return int(cur.fetchone()[0])

def get_total_comments():
    db, cur = get_db()
    statement = "SELECT COUNT (*) FROM comments"
    cur.execute(statement)
    return int(cur.fetchone()[0])

#GET FUNCTIONS USED FOR ADD FUNCTIONS

def get_next_user():
    db, cur = get_db()
    statement = "SELECT COUNT (*) FROM users"
    cur.execute(statement)
    return int(cur.fetchone()[0])+1
def get_next_post():
    db, cur = get_db()
    statement = "SELECT COUNT (*) FROM posts"
    cur.execute(statement)
    return int(cur.fetchone()[0])+1
def get_next_comment():
    db, cur = get_db()
    statement = "SELECT COUNT (*) FROM comments"
    cur.execute(statement)
    return int(cur.fetchone()[0])+1
    
#ALL ADD FUNCTIONS

def add_user (ID , Name , Username , Email , Street , Suite , City , Zipcode , LAT , LON , Phone , Website , CompanyName , CompanyCP , CompanyBS):
    db, cur = get_db()
    statement = "INSERT INTO users (ID , Name , Username , Email , Street , Suite , City , Zipcode , LAT , LON , Phone , Website , CompanyName , CompanyCP , CompanyBS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cur.execute(statement, [ID , Name , Username , Email , Street , Suite , City , Zipcode , LAT , LON , Phone , Website , CompanyName , CompanyCP , CompanyBS])
    db.commit()
    return True

def add_post (Title, ID, UserID, Body):
    db, cur = get_db()
    statement = "INSERT INTO posts(Title, ID, UserID, Body) VALUES (?,?,?,?)"
    cur.execute(statement, [Title, ID, UserID, Body])
    db.commit()
    return True

def add_comment (PostID, ID, Name, Email, Body):
    db, cur = get_db()
    statement = "INSERT INTO comments(PostID, ID, Name, Email, Body) VALUES (?,?,?,?,?)"
    cur.execute(statement,[PostID, ID, Name, Email, Body])
    db.commit()
    return True

#ALL DELETE FUNCTIONS

def delete_account(ID):
    db, cur = get_db()
    statement = "DELETE FROM users WHERE ID = ?"
    cur.execute(statement,[ID])
    db.commit()
    return True

def delete_post(ID):
    db, cur = get_db()
    statement = "DELETE FROM posts WHERE ID = ?"
    cur.execute(statement,[ID])
    db.commit()
    return True

def delete_comment(ID):
    db, cur = get_db()
    statement = "DELETE FROM comments WHERE ID = ?"
    cur.execute(statement,[ID])
    db.commit()
    return True

def delete_account_posts(ID):
    db, cur = get_db()
    statement = "DELETE FROM posts WHERE UserID = ?"
    cur.execute(statement,[ID])
    db.commit()

def delete_post_comments(ID):
    db, cur = get_db()
    statement = "DELETE FROM comments WHERE PostID = ?"
    cur.execute(statement,[ID])
    db.commit()
    return True








