import socket

# create a Socket.IO server
sio = socketio.AsyncServer()

# wrap with ASGI application
app = socketio.ASGIApp(sio, static_files=static_files)

static_files = {

}
