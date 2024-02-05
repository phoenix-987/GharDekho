import json
import pytest
from django.urls import reverse
from unittest.mock import patch


@pytest.mark.django_db
@patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True)
@pytest.mark.parametrize(
    'email, old_password, new_password, confirm_password, validity',
    [
        ('test@test.com', None, None, None, False),                              # Test case with no data::RESULT-FALSE
        ('test@test.com', 'password', None, None, False),                        # Test case with no new pwd::RESULT-FALSE
        ('test@test.com', 'wrong_pwd', 'new_password', None, False),             # Test case with no confirm pwd::RESULT-FALSE
        ('test@test.com', 'wrong_pwd', 'new_password', 'new_password', False),   # Test case with wrong password::RESULT-FALSE
        ('test@test.com', 'wrong_pwd', 'new_password', 'mismatch_pwd', False),   # Test case with wrong confirm pwd::RESULT-FALSE
        ('test@test.com', 'password', 'new_password', 'new_password', True),     # Test case with correct data::RESULT-TRUE
    ]
)
def test_change_password(db, client, create_dummy_user, email, old_password, new_password, confirm_password, validity):
    print(create_dummy_user)
    url = reverse('user-change-password')
    data = {
        'old_password': old_password,
        'new_password': new_password,
        'confirm_password': confirm_password
    }

    with patch('authorization.serializers.user_change_password_serializer.authenticate') as mock_authenticate:
        # with patch('authorization.serializers.user_change_password_serializer.authenticate') as mock_authenticate:
        mock_authenticate.return_value = create_dummy_user
        print('dummy-user', create_dummy_user)

        response = client.post(url, json.dumps(data), content_type='application/json')
        print('response', response)

        assert (response.status_code == 200) == validity
