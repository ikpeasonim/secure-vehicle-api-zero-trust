from phase_03_authorization_api import app, is_authorized, VEHICLE_PERMISSIONS

VALID_KEY = "dev-key-123"
INVALID_KEY = "bad-key"


def test_authorized_access():
    client = app.test_client()
    headers = {"X-API-KEY": VALID_KEY}

    # Pick a vehicle your role has access to
    vehicle_id = VEHICLE_PERMISSIONS["developer"][0]

    response = client.get(f"/status?vehicle_id={vehicle_id}", headers=headers)
    assert response.status_code == 200


def test_unauthorized_access():
    client = app.test_client()
    headers = {"X-API-KEY": INVALID_KEY}

    response = client.get("/status?vehicle_id=CAR123", headers=headers)
    assert response.status_code == 403


def test_authorization_logic():
    # Check VEHICLE_PERMISSIONS explicitly
    for role, vehicles in VEHICLE_PERMISSIONS.items():
        for vehicle in vehicles:
            assert is_authorized(role, vehicle) is True
        # Should fail for a vehicle not in their list
        assert is_authorized(role, "CAR999") is False
