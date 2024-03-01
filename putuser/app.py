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

@app.route ('/put_user',methods = ['PUT'])
def put_user():
    response = request.get_json()
    id_memo = response['id_memo']
    firstname = response['firstname']
    lastname = response['lastname']
    email = response['email']
#Update Data
    
    sql = "UPDATE memo SET firstname=%s, lastname=%s, email=%s"
    sql += "WHERE id_memo=%s"
    data = (firstname, lastname, email, id_memo)
    
    cur = conn.reconnect()
    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    conn.close()
    
    return redirect('http://127.0.0.1:5001/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)