from flask import Flask , render_template , url_for

app = Flask(__name__,static_folder='templates\static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods = ['POST','GET'])
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=200)
    