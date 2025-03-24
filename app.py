from flask import Flask
#a
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!111111111111111111111111111'

if __name__ == '__main__':
    app.run(debug=True) 