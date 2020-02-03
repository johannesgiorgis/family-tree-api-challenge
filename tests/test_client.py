import pytest

import sys
import os

# ensure pytest runs from project root directory
container_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, container_folder)

from family_tree.app import create_app


@pytest.fixture
def client():
    flask_app = create_app()
    flask_app.app.config["TESTING"] = True

    client = flask_app.app.test_client()
    yield client
