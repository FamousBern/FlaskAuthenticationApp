import os
DEBUG = True
SECRET_KEY = '\rj\xef\xe2\xec\xa9\x997\xc76U2\xf5\xf0\xfd\xa0P;\x80\x80Dt@\x9c\x7f\xf4\x81\x86\xa8\x87\x1bR\xfaO'
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydb.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = database_file