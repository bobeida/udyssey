from udyssey import app

@app.route('/')
def index():
    return 'Hello world!'