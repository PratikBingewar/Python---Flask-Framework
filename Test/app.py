from flask import Flask,redirect,url_for

### WSGI application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/pratik')
def hello_pratik():
    return 'Hello, Pratik!'

@app.route('/success/<int:score>')
def success(score):
    return 'The peron has passed and the score is '+ str(score)

@app.route('/failed/<int:score>')
def failed(score):
    return 'The peron has falied and the score is '+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = 0
    if marks < 50:
        result = 'failed'
    else:
        result = 'passed'
        
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run()
