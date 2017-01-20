from flask import Flask, render_template
import random
app = Flask(__name__)
temperatures = [25,14,17,20,20,21,23,17,20,20,17]
humidities = [72,65,61,62,79,62,66,53,51,71]

@app.route('/')
def index():
    return render_template('index.html.j2', temp=random.choice(temperatures), humid=random.choice(humidities))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
