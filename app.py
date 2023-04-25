import os
from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.7'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('aulamcv.html')

@app.route('/gravar', methods=['POST','GET'])
def formulario():
    name = request.form ['nome']
    email = request.form ['email']
    senha = request.form ['senha']
    print (senha)
    cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s,%s,%s)' , (name, email,senha))
    conn.commit()

    return render_template('aulamvc.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


