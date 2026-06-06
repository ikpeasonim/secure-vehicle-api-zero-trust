from phase_02_authenticated_api import app


VALID_KEY = "dev-key-123"
INVALID_KEY = "bad-key"


def test_missing_api_key():
    client = app.test_client()

    response = client.get(
        "/status?vehicle_id=CAR123"
    )

    assert response.status_code == 401


def test_invalid_api_key():
    client = app.test_client()

    response = client.get(
        "/status?vehicle_id=CAR123",
        headers={"X-API-KEY": INVALID_KEY}
    )

    assert response.status_code == 403


def test_valid_api_key():
    client = app.test_client()

    response = client.get(
        "/status?vehicle_id=CAR123",
        headers={"X-API-KEY": VALID_KEY}
    )

    assert response.status_code == 200
