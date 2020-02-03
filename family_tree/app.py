from flask_cors import CORS  # To work with Connexion
import connexion


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir="swagger/")
    app.add_api("familytree_api.yml")

    CORS(app.app)

    return app
