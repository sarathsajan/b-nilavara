from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'



'''
app.config['SECRET_KEY'] = appdata['app-secret-key']
app.config.from_pyfile('config.cfg')

# Configuring MySQL Database
app.config['MYSQL_HOST'] = 'localhost'                                                  # localhost
#app.config['MYSQL_HOST'] = 'amisafe.mysql.pythonanywhere-services.com'                  # amisafe
app.config['MYSQL_USER'] = 'root'                                                       # localhost
#app.config['MYSQL_USER'] = 'amisafe'                                                    # amisafe
app.config['MYSQL_PASSWORD'] = appdata['database-password']                             # localhost
#app.config['MYSQL_PASSWORD'] = appdata['database-password']                             # amisafe
app.config['MYSQL_DB'] = 'cross_path_alert'                                             # localhost
#app.config['MYSQL_DB'] = 'amisafe$amisafe'                                                      # amisafe
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#app.config['MYSQL_PORT'] = 3306                                                         # if not in localhost, uncomment this

mysql = MySQL(app)
'''



@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
