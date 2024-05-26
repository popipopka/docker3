from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_data():
    return 'Данные от сервера после GET запроса'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
