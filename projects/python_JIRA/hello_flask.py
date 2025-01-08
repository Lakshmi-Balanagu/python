from flask import Flask

app = Flask(__name__) #creating a flask app instance

#using decorates .Decorates starts with @
#Main purpose of decorater is before invoek the function it's need to execute @ action.

@app.route("/")
def hello():
    return 'Hello World'

app.run('0.0.0.0')

