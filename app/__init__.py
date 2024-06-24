# from flask import Flask
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from .routes import main_blueprint
# from .qaroutes import qa_blueprint
# from .dcroutes import dc_blueprint
# # from .ggsroutes import ggs_blueprint  # Uncomment when implementing


# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config')

#     CORS(app)
#     db.init_app(app)
#     migrate = Migrate(app, db)

#     app.register_blueprint(main_blueprint, url_prefix='/')
#     app.register_blueprint(qa_blueprint, url_prefix='/api/question-assistant')
#     app.register_blueprint(dc_blueprint, url_prefix='/api/document-chat')
#     # app.register_blueprint(ggs_blueprint, url_prefix='/api/good-gov-screener')  # Uncomment when implementing

#     return app



from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:test:"
    app.config.from_object('config')

    CORS(app)
    db.init_app(app)
    Migrate(app, db)

    # Import and register blueprints inside the create_app function to avoid circular imports
    from .routes import main_blueprint
    from .qaroutes import qa_blueprint
    from .dcroutes import dc_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(qa_blueprint, url_prefix='/api/question-assistant')
    app.register_blueprint(dc_blueprint, url_prefix='/api/document-chat')
    # from .ggsroutes import ggs_blueprint  # Uncomment when implementing
    # app.register_blueprint(ggs_blueprint, url_prefix='/api/good-gov-screener')

    return app