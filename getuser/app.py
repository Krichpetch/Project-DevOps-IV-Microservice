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


app.staticfolder = 'static'
app.static_url_path = "/static"


#Rest API
@app.route ("/getuser/v1/<id_memo>", methods = ['GET'])
def get_user(id_memo):
    cur = conn.reconnect()
    
    sql = "SELECT id_memo, firstname, lastname, email "
    sql += " FROM memo WHERE id_memo = %s ORDER BY firstname"
    data = (id_memo,)
    cur = conn.cursor()
    cur.execute(sql,data)
    records = cur.fetchall()
    conn.close()
    return jsonify(records)

@app.route('/getuser', methods = ["GET"])     
def get_user_all():
    cur = conn.reconnect() 
    
    sql = "SELECT id_memo, firstname, lastname, email "
    sql += " FROM memo ORDER BY firstname" 
    cur = conn.cursor()  
    cur.execute(sql)
    records = cur.fetchall()
    conn.close()
    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)