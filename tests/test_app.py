from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    unique_email = "temp-student@example.com"

    signup_response = client.post(
        "/activities/Chess Club/signup",
        params={"email": unique_email},
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": unique_email},
    )
    assert unregister_response.status_code == 200

    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert unique_email not in activities["Chess Club"]["participants"]
