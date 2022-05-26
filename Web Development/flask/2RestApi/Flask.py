from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome to TestApi. Put a /name on URL to get a json'


@app.route('/users')
def index():
    name = request.args.get('name')
    age = request.args.get('age')
    r = {'name': name,
         'age': age}
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)
