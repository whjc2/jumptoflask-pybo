from flask import Flask
from flask_migrate import Migrate
#from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

#app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    #from jumptoflask import models
    import models


    from views import main_views, question_views
    #app.register_blueprint(main_views.bp)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app