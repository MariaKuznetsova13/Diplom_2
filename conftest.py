import pytest
from helpers import generate_user_credentials, delete_user


@pytest.fixture(scope='function')
def user():
    credentials = generate_user_credentials()
    yield credentials
    delete_user(credentials)
