from flask import *
from flask_socketio import SocketIO, emit

Server = Flask(__name__)
    
@Server.route('/', methods=['GET'])
def home():
    return render_template("index.html")



Flask.run(Server,host='', port=8000)