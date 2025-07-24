from flask import Flask
from routes.form import form_route
from routes.api import api_route

app = Flask(__name__)

app.register_blueprint(form_route)
app.register_blueprint(api_route)


# if __name__ == '__main__':
#     app.run(debug=True)
#     app.run(host='0.0.0.0', port=5000, debug=False)