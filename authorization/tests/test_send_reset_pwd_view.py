import json
import pytest
from django.urls import reverse


# Parameterize marker to test the cases.
@pytest.mark.parametrize(
    'email',
    ['s.kir001990@gmail.com', 'test@test.com', 'naman.j@consultadd.com']        # Test case with all data::RESULT-PASS
)
def test_send_reset_pwd_view(db, create_dummy_user, email, client):
    url = reverse('user-reset-password-mail')
    data = {
        'email': email
    }

    response = client.post(url, json.dumps(data), content_type='application/json')
    assert response.status_code == 200
