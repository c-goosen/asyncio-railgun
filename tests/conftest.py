from asyncio import get_event_loop
import pytest


@pytest.fixture
def event_loop():
    return get_event_loop()