import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)

    with app.test_client() as client:
        yield client


def test_application_loads():
    assert app is not None


def test_routes_are_registered():
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    assert len(routes) > 0
