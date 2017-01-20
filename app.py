from flask import Flask, render_template
app = Flask(__name__)
temperatures = [25,14,17,20,20,21,23,17,20,20,17]
humidities = [72,65,61,62,79,62,66,53,51,71]
temp = 25
humidity = 72

@app.route('/')
def index():
    return render_template('index.html', temp=temp, humidity=humid)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
