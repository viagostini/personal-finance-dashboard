def create_two_users(test_client):
    test_client.post(
        '/users/',
        json={"email": "test@example.com", "password": "testpassword"}
    )
    test_client.post(
        '/users/',
        json={"email": "anothertest@example.com", "password": "anotherpassword"}
    )


def create_two_items(test_client):
    test_client.post(
        '/items/?user_id=1',
        json={"title": "TestItem", "description": "This is a test description"}
    )
    test_client.post(
        '/items/?user_id=2',
        json={"title": "AnotherTestItem", "description": "This is another test description"}
    )


def test_users_with_items(test_client):
    create_two_users(test_client)
    create_two_items(test_client)

    response = test_client.get('/users/')
    assert response.status_code == 200
    assert response.json() == [
        {
            "email": "test@example.com",
            "id": 1,
            "items": [
                {
                    "title": "TestItem",
                    "description": "This is a test description",
                    "id": 1,
                    "owner_id": 1
                }
            ]
        },
        {
            "email": "anothertest@example.com",
            "id": 2,
            "items": [
                {
                    "title": "AnotherTestItem",
                    "description": "This is another test description",
                    "id": 2,
                    "owner_id": 2
                }
            ]
        }
    ]