import pytest
from app.app import create_app
from flask_migrate import upgrade

@pytest.fixture
def client():
    app = create_app()

    with app.app_context():
        upgrade()
        yield app.test_client()


