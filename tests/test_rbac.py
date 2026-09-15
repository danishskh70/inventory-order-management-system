def test_protected_route_requires_auth(client):
    response = client.get("/products/")
    assert response.status_code == 401


def test_create_order_without_role_forbidden(client):
    client.post("/users/", json={
        "name": "No Role User",
        "username": "norole1",
        "password": "testpass123"
    })

    login = client.post("/auth/login", json={
        "username": "norole1",
        "password": "testpass123"
    })
    token = login.json()["access_token"]

    response = client.post(
        "/orders/",
        json={"customer_id": 1, "status": "pending"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 403