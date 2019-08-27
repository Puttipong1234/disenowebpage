from flask import Flask , render_template , url_for

app = Flask(__name__,static_folder='templates/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods = ['POST','GET'])
def contact():
    return render_template('contact.html')

@app.route('/model', methods = ['POST','GET'])
def model():
    return render_template('model.html')


if __name__ == '__main__':
    app.run(port=200)
    