from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<html><body><div id="hello"></div><script src="http://dockerhost:8000/bundle.js"></script></body></html>'

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
