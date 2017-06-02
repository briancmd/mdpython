from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_page():
    return 'This is the index page!'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/projects/')
def hello_projects():
    return 'This is the project page!'

if __name__ == '__main__':
    app.run()
