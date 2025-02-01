from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return ('hello world')
@app.route('/about')
def about():
    return 'About Page'
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/home')
def home():
    return 'Home Page'

