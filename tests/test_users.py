import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_create_user_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/users", json={"name": "Alice", "age": 25})
    assert response.status_code == 200
    assert response.json() == {"name": "Alice", "age": 25}

@pytest.mark.asyncio
async def test_create_user_invalid_age():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/users", json={"name": "Bob", "age": -1})
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid age"}

@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First ensure there's at least one user
        await ac.post("/users", json={"name": "Charlie", "age": 30})
        response = await ac.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) >= 1
    assert {"name": "Charlie", "age": 30} in users
