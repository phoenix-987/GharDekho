import pytest
from faker import Faker
from authorization.models import User


@pytest.mark.django_db
@pytest.fixture
def create_dummy_user(email):
    if email is None or 'kir' not in email:
        return None

    User.objects.create_user(
        email=email,
        name=Faker().name(),
        password=Faker().password(),
        is_owner=False
    )
