import http.server
import socketio

PORT = 5000

sio = socketio.Client()

@sio.on('my message')
def on_message(data):
    print('I received a message!')

