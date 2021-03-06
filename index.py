from flask import Flask, redirect, url_for, request
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
   print('Message: '+ msg)
   socketio.send(msg, broadcast = True)

if __name__ == '__main__':
   socketio.run(app) 