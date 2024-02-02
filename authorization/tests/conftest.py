import pytest
from faker import Faker
from authorization.models import User


@pytest.mark.django_db
@pytest.fixture
def create_dummy_user(email):
    if email is None:
        return None

    user = User.objects.create_user(
        email=email,
        name=Faker().name(),
        password='password',
        is_owner=False
    )

    return user
