from flask import Flask, request, jsonify
import database_connection
# import sqlite3


# def create_database():
# connect = sqlite3.connect('example.db')
# c = connect.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS users(
#             first_name text,
#             last_name text,
#             id int
#         )''')

# connect.commit()
# connect.close()
# connect = sqlite3.connect('example.db')
# print(connect)

# # create_database()

# c = connect.cursor()
# many_users = [
#                     ('Annie', 'Vu', '123'),
#                     ('Linh', 'Tran', '234'),
#                     ('Raina', 'Qiu', '345')
# ]

# c.executemany("INSERT INTO users(first_name, last_name, id) VALUES(?, ?, ?)", many_users)
# connect.commit()
# print(c.fetchall())
# connect.close()


# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     return "Hello World", 200


# def receive_data():

#     user_data = {
#         user_id : user_id,
#         "name": "John Doe",
#         "email" : "john.doe@example.com"

#     }

#     connect = sqlite3.connect('example.db')
#     c = connect.cursor()



#     c.execute('SELECT * FROM users')
#     rows = c.fetchall()
#     print(rows)

#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra


#     return jsonify(rows), 200

# def receive_info(info, db_name='example.db'):
#     connect = sqlite3.connect('example.db')
#     c = connect.cursor()

#     json_string = json.dumps(info)
#     c.execute("INSERT INTO jsonData (data) VALUES (?)", (json_string,))
#     connect.commit()



# def home()
#     return "Home" 

if __name__ == "__main__":
    #app.run(debug=True)
    database_connection.test()
    database_connection.add_data()