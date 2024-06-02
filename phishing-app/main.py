from socketio import Client

sio = Client()

@sio.event
def connect():
    print("Connected to the server")

@sio.event
def form_data(data):
    login = data['login']
    password = data['password']
    print(f"Login: {login}, Password: {password}")

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')