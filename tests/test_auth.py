def test_register_user(client):
    response = client.post("/users/", json={
        "name": "Test User",
        "username": "testuser1",
        "password": "testpass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser1"
    assert "password" not in data


def test_login_success(client):
    client.post("/users/", json={
        "name": "Test User",
        "username": "testuser2",
        "password": "testpass123"
    })

    response = client.post("/auth/login", json={
        "username": "testuser2",
        "password": "testpass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post("/users/", json={
        "name": "Test User",
        "username": "testuser3",
        "password": "testpass123"
    })

    response = client.post("/auth/login", json={
        "username": "testuser3",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    