from flask import Flask, request
import twilio.twiml
from models import Message
from commands import commands


SUPER_SECRET_KEY = "MySuperSercretKey"

app = Flask(__name__, static_url_path='')


def handleMessage(message):
    if len(message.body) < 1:
        return commands['unknown'](message)

    command = message.body.split(" ")[0]
    command = command.lower()

    if command in commands.keys():
        return commands[command](message)
    else:
        return commands['search'](message)


@app.route("/", methods=['GET', 'POST'])
def home():
    return app.send_static_file('index.html')


@app.route("/"+SUPER_SECRET_KEY, methods=['GET', 'POST'])
def refuge():
    """Handle incoming SMS messages"""

    msg = Message(request.values)
    command = None
    message = ""

    if msg is None or msg.from_number is None:
        return commands['unknown'](message)

    return handleMessage(message)


@app.route("/robots.txt", methods=['GET'])
def robots():
    return app.send_static_file('robots.txt')


if __name__ == "__main__":
    app.run(debug=True)
