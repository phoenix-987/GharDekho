# import pytest
# from authorization.models import User
# from authorization.serializers import UserSerializer
#
#
# # Parameterize marker to test the cases.
# @pytest.mark.parametrize(
#     'email, name, is_owner, password, confirm_password, validity',
#     [
#         (None, None, None, None, None, False),                                     # Test case for no data::RESULT-FALSE
#         (None, 'Tester', False, 'password', 'password', False),                   # Test case for no email::RESULT-FALSE
#         ('test@test.com', None, False, 'password', 'password', False),             # Test case for no name::RESULT-FALSE
#         ('test@test.com', 'Tester', None, 'password', 'password', False),  # Test case for no owner status::RESULT-FALSE
#         ('test@test.com', 'Tester', False, None, 'password', False),           # Test case for no password::RESULT-FALSE
#         ('test@test.com', 'Tester', False, 'password', None, False),   # Test case for no confirm password::RESULT-FALSE
#         ('test@test.com', 'Tester', False, 'password', 'mismatch_password', False),  # Test case for mismatch passwords::RESULT-FALSE
#         ('test@test.com', 'Tester', True, '', '', False),                     # Test case for no passwords::RESULT-FALSE
#         ('test@test.com', 'Tester', False, 'password', 'password', True),       # Test case for all correct details::RESULT-TRUE
#     ]
# )
# def test_user_serializer(db, email, name, is_owner, password, confirm_password, validity):
#     data = {
#         'email': email,
#         'name': name,
#         'is_owner': is_owner,
#         'password': password,
#         'confirm_password': confirm_password
#     }
#
#     try:
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#
#         count = User.objects.all().count()
#         assert validity == count
#
#     except Exception:
#         assert not validity
