from flask import Flask, request, render_template, redirect, jsonify
import mysql.connector as mysql

conn = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '29012547',
    port =  3306,
    database = 'my_memo'
)

app = Flask(__name__)

@app.route ('/delete/<email>', methods = ['DELETE'])
def delete_user (email):
    # response = request.get.json()
    # email = response['email']
    cur = conn.reconnect()
    cur = conn.cursor()
    sql = "DELETE FROM memo WHERE email=%s "
    data = (email,)
    cur.execute(sql,data)
    conn.commit()
    conn.close()
    return redirect ('http://127.0.0.1:5001/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)