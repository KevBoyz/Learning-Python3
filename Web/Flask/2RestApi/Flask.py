from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def root():
    return 'Welcome to TestApi. Put a /name on URL to get a json'


@app.route('/users/', defaults={'name': 'KevBoyz', 'age': 15})
@app.route('/users/<name>/<age>')
def index(name, age):
    get_name = request.args.get('name')
    get_age = request.args.get('age')
    if get_name:
        name = get_name
    if get_age:
        age = get_age
    r = {'name': name,
         'age': age}
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)
