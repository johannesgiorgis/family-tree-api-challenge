from flask_cors import CORS  # To work with Connexion
import connexion


from family_tree.views import health_check


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir="swagger/")
    app.add_api("swagger.yml")

    # register blueprints
    app.app.register_blueprint(health_check.blueprint, url_prefix="/api")

    CORS(app.app)

    return app
