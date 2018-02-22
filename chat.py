from flask import Flask,request
from flask_socketio import SocketIO,send,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

print("ATARTING")
sockets = []
mobile = []
clients = []
#sockets[0] = socketio

@socketio.on('myConnect')
def handleconnect(json):
	print('in MYCONNECT')
	print(str(json))
	mobile.append(json['fromMobile'])
	print(mobile)
	sockets.append(socketio)
	print(sockets)

	clients.append(request.sid)

	
#	print('Message is ' + msg)
#	print('from mobile' + str(fromMobile))
#	sockets.append(socketio)

@socketio.on('myMessage')
def handlemessage(json):
	print('in MYMESSAGE',str(json))
	print('the message',json['msg'])
	tp_index = mobile.index(json['toMobile'])
	print('tp_index=',tp_index)
#	socketio.to(sockets[tp_index]).emit('message',json['msg'])
	emit('message',json['msg'],room=clients[tp_index])
#	print('Message is ' + msg)
#	print('from mobile' + str(fromMobile))
#	print('to Mobile' + str(toMobile))
#	socketio.emit()
#	send(msg,broadcast=True)

@socketio.on('message')
def handlemessage2(msg):
	print('in message handler '+msg)

if __name__ == '__main__':
	socketio.run(app)
