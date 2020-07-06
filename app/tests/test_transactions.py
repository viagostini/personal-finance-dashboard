from datetime import datetime

def test_create_transaction(test_client):
    # time_now = datetime.strptime("2020-07-05 21:27:05.145132", "%Y-%m-%d %H:%M:%S.%f"),
    response = test_client.post(
        '/transactions/?account_id=1',
        json={
            "title": "TestTransaction",
            "value": 24.90,
            # "timestamp": time_now
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "TestTransaction",
        "id": 1,
        "value": 24.90,
        "account_id": 1,
        "category": "Other",
        "type": "expense",
        "description": None
        # "timestamp": time_now,
    }

