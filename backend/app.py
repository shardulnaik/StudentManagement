from flask import Flask
from flask_cors import CORS
from routes import register_routes
from config import Config
from models import db

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

db.init_app(app)

register_routes(app)
@app.route("/")
def home():
    return "Student Management System Backend Running"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)