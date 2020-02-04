"""
Health Check Test
-----------------

Check that the health check is working
"""

from flask import Response


def test_health_check(client):
    resp: Response = client.get("/api/health_check")

    assert resp.status_code == 200
