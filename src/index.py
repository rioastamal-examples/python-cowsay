from flask import Flask
from flask import request
import cowsay

app = Flask(__name__)

@app.route('/')
def main():
    text = request.args.get('text')
    if text == None:
        text = '''\
I do not understand what you're saying!
.
Usage:
/?text=TEXT
.
Where:
 TEXT is text you want to say.\
'''

    the_text = cowsay.get_output_string('cow', text)
    return the_text, 200, { 'content-type': 'text/plain' }
