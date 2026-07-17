from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    # Arrange
    unique_email = "temp-student@example.com"

    # Act
    signup_response = client.post(
        "/activities/Chess Club/signup",
        params={"email": unique_email},
    )

    unregister_response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": unique_email},
    )

    activities_response = client.get("/activities")
    activities = activities_response.json()

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert unique_email not in activities["Chess Club"]["participants"]
