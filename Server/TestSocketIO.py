import socketio
import eventlet

io = socketio.Server()
app = socketio.WSGIApp(io)

@io.event
def connect(sid, environ):
    print('connect ', sid)
    print(environ)  

@io.event
def message(sid, data):
    print('message ', data)
 
@io.event
def disconnect(sid):
    print('disconnect ', sid)

eventlet.wsgi.server(eventlet.listen(('localhost',5000)),app) 