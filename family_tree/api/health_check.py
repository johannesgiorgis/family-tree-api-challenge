"""
API Health Check
"""

from flask import jsonify


def health_check():
    return jsonify(True)
