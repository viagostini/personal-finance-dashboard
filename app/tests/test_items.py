def test_create_item(test_client):
    response = test_client.post(
        '/items/?user_id=1',
        json={"title": "TestItem", "description": "This is a test description"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "TestItem",
        "description": "This is a test description",
        "id": 1,
        "owner_id": 1
    }

def test_get_items_empty(test_client):
    response = test_client.get('/items/')
    assert response.status_code == 200
    assert response.json() == []

def test_get_items(test_client):
    test_client.post(
        '/items/?user_id=1',
        json={"title": "TestItem", "description": "This is a test description"}
    )
    test_client.post(
        '/items/?user_id=1',
        json={"title": "AnotherTestItem", "description": "This is another test description"}
    )

    response = test_client.get('/items')
    assert response.status_code == 200
    assert response.json() == [
        {
            "title": "TestItem",
            "description": "This is a test description",
            "id": 1,
            "owner_id": 1
        },
        {
            "title": "AnotherTestItem",
            "description": "This is another test description",
            "id": 2,
            "owner_id": 1
        }
    ]