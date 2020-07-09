from app.routers import transactions


def create_two_users(test_client):
    test_client.post(
        '/users/',
        json={"email": "test@example.com", "password": "testpassword"}
    )
    test_client.post(
        '/users/',
        json={"email": "anothertest@example.com", "password": "anotherpassword"}
    )


def create_two_accounts(test_client):
    test_client.post(
        '/accounts/?user_id=1',
        json={"name": "TestAccount"}
    )
    test_client.post(
        '/accounts/?user_id=2',
        json={"name": "AnotherTestAccount"}
    )


def create_two_transactions(test_client):
    test_client.post(
        '/transactions/?account_id=1',
        json={
            "title": "TestTransaction",
            "value": 24.90,
        }
    )
    test_client.post(
        '/transactions/?account_id=2',
        json={
            "title": "AnotherTestTransaction",
            "value": 1337.42,
            "description": "TestDescription",
            "category": "TestCategory"
        }
    )



def test_users_with_accounts(test_client):
    create_two_users(test_client)
    create_two_accounts(test_client)
    create_two_transactions(test_client)

    response = test_client.get('/users/')
    assert response.status_code == 200
    assert response.json() == [
        {
            "email": "test@example.com",
            "id": 1,
            "accounts": [
                {
                    "name": "TestAccount",
                    "id": 1,
                    "owner_id": 1,
                    "transactions": [
                        {
                            "id": 1,
                            "title": "TestTransaction",
                            "value": 24.90,
                            "description": None,
                            "category": "Other",
                            "type": "expense",
                            "account_id": 1
                        }
                    ]
                }
            ]
        },
        {
            "email": "anothertest@example.com",
            "id": 2,
            "accounts": [
                {
                    "name": "AnotherTestAccount",
                    "id": 2,
                    "owner_id": 2,
                    "transactions": [
                        {
                            "id": 2,
                            "title": "AnotherTestTransaction",
                            "value": 1337.42,
                            "description": "TestDescription",
                            "category": "TestCategory",
                            "type": "expense",
                            "account_id": 2
                        }
                    ]
                }
            ]
        }
    ]