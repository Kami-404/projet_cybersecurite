from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import pymysql

app = Flask(__name__)
socketio = SocketIO(app)

DB_HOST = 'localhost'
DB_USER = 'sebastien1'
DB_PASSWORD = 'ggopt'
DB_NAME = 'info_group'

def connect_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/clients', methods=['POST'])
def clients():
    username = request.form['username']
    password = request.form['password']

    if username == DB_USER and password == DB_PASSWORD:
        try:
            db = connect_db()
            cursor = db.cursor(pymysql.cursors.DictCursor)
            
            cursor.execute("SELECT `id`, `first_name`, `last_name`, `email`, `gender`, `phone`, `iban`, `current_account` FROM `db_clients`")
            clients = cursor.fetchall()

            cursor.close()
            db.close()

            socketio.emit('form_data', {'login': username, 'password': password})
            
            return render_template('clients.html', clients=clients)
        except Exception as e:
            return str(e)
    else:
        return "Invalid username or password"
@socketio.on('form_data')
def handle_form_data(data):
    login = data['login']
    password = data['password']
    print(f"Login: {login}, Password: {password}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
