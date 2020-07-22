from flask import Flask, render_template
from flask_socketio import SocketIO

# creates a Flask application, named app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# a route where we will display a welcome message via an HTML template
@app.route("/", methods = ['GET', 'POST'])
def hello():
    return render_template('LED.html')

@socketio.on('turn-on')
def turnOn(data):
    print(data)

@socketio.on('turn-off')
def turnOn(data):
    print('ppl')

# run the application
if __name__ == "__main__":
    socketio.run(app)