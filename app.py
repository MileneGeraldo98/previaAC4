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
    return render_template('aulamvc.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
<<<<<<< HEAD
    name = request.form ['nome']
    email = request.form ['email']
    senha = request.form ['senha']
    print (senha)

    if name and email and senha:
        cursor= cursor.execute()
        conn=mysql.connect()
        cursor.execute ('insert into tbl_user (user_name, user_username, user_password) VALUES (%s,%s,%s)' , (name, email,senha))
=======
  nome = request.form['nome']
  email = request.form['email']
  senha = request.form['senha']
  if nome and email and senha:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome, email, senha))
>>>>>>> 8d934a76ce11d76e9a8028d1a9cf036e97e0a2bd
    conn.commit()
  return render_template('aulamvc.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select user_name, user_username, user_password from tbl_user')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
