from flask import Flask, render_template
import data
import logging
app = Flask(__name__)
app.config.from_object(__name__)

logging.basicConfig(filename='app.log', level=logging.DEBUG)

app.config.update(dict(
    SECRET_KEY = 'dev key'
    USERNAME = 'admin'
    PASSWORD = 'password'
))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    #data.start_reading_data()
