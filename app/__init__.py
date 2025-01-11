from flask import Flask
#from flask_migrate import Migrate
#from database.models import db  # Assuming this is where your db is defined
from config import Config  # Config file for settings

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Load configurations from the Config class
    app.config.from_object(Config)

    # Initialize the database with the app
   # db.init_app(app)
    
 

    # Initialize Flask-Migrate for database migrations
    # migrate = Migrate(app, db)

    # Register blueprints for routes
    from .routes.feedback_routes import feedback_routes
    from .routes.visualization_routes import visualization_bp
    from .routes.account_routes import account_bp
    from .routes.reservation_routes import reservation_bp
    
   # from .routes.auth_routes import auth_bp
    from .routes.main_routes import main_bp  # Import main routes blueprint

    # Register the blueprints
    app.register_blueprint(main_bp)  # Register the main blueprint (no prefix)
    app.register_blueprint(feedback_routes, url_prefix='/feedback')
    app.register_blueprint(visualization_bp, url_prefix='/account')
    app.register_blueprint(account_bp, url_prefix='/training')
    app.register_blueprint(reservation_bp, url_prefix='/reservation')
    # app.register_blueprint(auth_bp, url_prefix='/auth')

    return app





