def test_create_account(test_client):
    response = test_client.post(
        '/accounts/?user_id=1',
        json={"name": "TestItem"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "TestItem",
        "id": 1,
        "owner_id": 1,
        "transactions": []
    }

def test_get_accounts_empty(test_client):
    response = test_client.get('/accounts/')
    assert response.status_code == 200
    assert response.json() == []

def test_get_accounts(test_client):
    test_client.post(
        '/accounts/?user_id=1',
        json={"name": "TestItem"}
    )
    test_client.post(
        '/accounts/?user_id=1',
        json={"name": "AnotherTestItem"}
    )

    response = test_client.get('/accounts')
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "TestItem",
            "id": 1,
            "owner_id": 1,
            "transactions": []
        },
        {
            "name": "AnotherTestItem",
            "id": 2,
            "owner_id": 1,
            "transactions": []
        }
    ]