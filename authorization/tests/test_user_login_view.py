# import json
# import pytest
# from django.urls import reverse
# from unittest.mock import patch
#
#
# @pytest.mark.django_db
# @pytest.mark.parametrize(
#     'email, password, validity',
#     [
#         ('test@test.com', 'password', True),
#         ('test@gmail.com', 'password', True),
#         ('test@example.com', 'password', True),
#     ]
# )
# def test_user_login_view(client, create_dummy_user, email, password, validity):
#     url = reverse('user-login')
#     data = {
#         'email': email,
#         'password': password
#     }
#
#     with patch('authorization.views.user_login_view.authenticate') as mock_authenticate:
#         mock_authenticate.return_value = create_dummy_user
#         response = client.post(url, json.dumps(data), content_type='application/json')
#         print(response)
#
#         assert (response.status_code == 200) == validity
