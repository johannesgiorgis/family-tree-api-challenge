from flask import Blueprint
from flask import jsonify

blueprint = Blueprint("health_check", __name__)


@blueprint.route("/health_check", methods=["GET"])
def health_check():
    return jsonify(True)
