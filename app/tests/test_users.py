def test_get_users_empty(test_client):
    response = test_client.get('/users/')
    assert response.status_code == 200
    assert response.json() == []


def test_create_user(test_client):
    response = test_client.post(
        '/users/',
        json={"email": "test@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "email": "test@example.com",
        "id": 1,
        "accounts": []
    }


def test_get_users(test_client):
    test_client.post(
        '/users/',
        json={"email": "test@example.com", "password": "testpassword"}
    )
    test_client.post(
        '/users/',
        json={"email": "anothertest@example.com", "password": "anotherpassword"}
    )

    response = test_client.get('/users')
    assert response.status_code == 200
    assert response.json() == [
        {
            "email": "test@example.com",
            "id": 1,
            "accounts": []
        },
        {
            "email": "anothertest@example.com",
            "id": 2,
            "accounts": []
        }
    ]