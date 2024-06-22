from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def calc(a,b):
    return a+b

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)

#this is called application server 
#opens http server 