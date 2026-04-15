import copy
import pytest

from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(scope="function")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def activities_reset():
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)
