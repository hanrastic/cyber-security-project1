from os import getenv
from app import app
from flask_sqlalchemy import SQLAlchemy

#uri = os.getenv("DATABASE_URL")  # or other relevant config var
#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://", 1)

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)
=======
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)
>>>>>>> 964dc06d8a9003ccf9c8d0815478423ca6ae3acb
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
