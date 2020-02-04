"""
Family Tree REST API Server
"""


from flask_cors import CORS  # To work with Connexion

import family_tree.config as config


def create_app():
    app = config.connex_app
    app.add_api("familytree_api.yml")

    config.db.init_app(app.app)

    CORS(app.app)

    return app
