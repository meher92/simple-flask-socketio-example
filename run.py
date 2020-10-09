from flask import *
from flask_socketio import *
import time

# Init the server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some super secret key!'
socketio = SocketIO(app, logger=True)

payload_template = {'text':'Message recieved counter {}'}

# Send HTML!
@app.route('/')
def root():
    return render_template('index.html')

# Returns a random number
@app.route('/random')
def random():
    from random import randint
    html = str(randint(1, 100))
    return html

# # Prints the user id
# @app.route('/user/<id>')
# def user_id(id):
#     return str(id)

# # Display the HTML Page & pass in a username parameter
# @app.route('/html/<username>')
# def html(username):
#     return render_template('index.html', username=username)

# Receive a message from the front end HTML
@socketio.on('send_message')
def message_recieved(data):
    print(data['text'])
    if data['text'] == "Server please start sending your shit":
        for i in range(5):
            payload = payload_template.copy()
            payload['text'] = payload['text'].format(i+1)
            emit('message_from_server', payload)
            time.sleep(3)

# Actually Start the App
if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=8000)
