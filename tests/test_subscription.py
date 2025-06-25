import pytest
import httpx
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_user_is_subscribed():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(base_url="http://test", transport=transport) as ac:
        response = await ac.post(
            "/check-subscription", json={"user_id": 687899499, "channel": "@iudalab"}
        )
        assert response.status_code == 200
        assert response.json() == {"subscribed": True}


@pytest.mark.asyncio
async def test_user_is_not_subscribed():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(base_url="http://test", transport=transport) as ac:
        response = await ac.post(
            "/check-subscription", json={"user_id": 999999999, "channel": "@iudalab"}
        )
        assert response.status_code == 200
        assert response.json() == {"subscribed": False}


@pytest.mark.asyncio
async def test_invalid_channel():
    transport = httpx.ASGITransport(app=app)
    async with AsyncClient(base_url="http://test", transport=transport) as ac:
        response = await ac.post(
            "/check-subscription",
            json={"user_id": 687899499, "channel": "@nonexistent_channel_123"},
        )
        assert response.status_code == 200
        assert response.json() == {"subscribed": False}
