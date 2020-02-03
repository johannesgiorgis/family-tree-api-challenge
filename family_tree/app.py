from flask_cors import CORS  # To work with Connexion
import connexion

from pathlib import Path

import family_tree.data.db_session as db_session


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir="swagger/")
    app.add_api("familytree_api.yml")

    setup_db()

    CORS(app.app)

    return app


def setup_db():
    """
    setup database
    """
    db_file = str(Path(__file__).parent.absolute().joinpath("db").joinpath("family.sqlite"))
    db_session.global_init(db_file)
