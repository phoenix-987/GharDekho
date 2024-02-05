# import pytest
# from authorization.serializers import UserChangePasswordSerializer
#
#
# # Parameterize marker to test the cases.
# @pytest.mark.parametrize(
#     'email, old_password, new_password, confirm_password, validity',
#     [
#         ('test@test.com', None, None, None, False),                                  # Test case for no data::RESULT-FALSE
#         ('test@test.com', None, 'new_password', 'new_password', False),              # Test case for no old password::RESULT-FALSE
#         ('test@test.com', 'password', None, 'new_password', False),                  # Test case for no new password::RESULT-FALSE
#         ('test@test.com', 'password', 'new_password', None, False),                  # Test case for no confirm password::RESULT-FALSE
#         ('test@test.com', 'old_password', 'new_password', 'new_password', False),    # Test case for wrong old password::RESULT-FALSE
#         ('test@test.com', 'password', 'new_password', 'mismatch_password', False),   # Test case for mismatch new and confirm password::RESULT-FALSE
#         ('test@test.com', 'password', 'new_password', 'new_password', True),         # Test case with all correct data::RESULT-TRUE
#     ]
# )
# def test_change_password_serializer(db, create_dummy_user, email, old_password, new_password, confirm_password, validity):
#     try:
#         # Testing Serializer by calling it with required value.
#         data = {'old_password': old_password, 'new_password': new_password, 'confirm_password': confirm_password}
#         serializer = UserChangePasswordSerializer(data=data, context={'user': create_dummy_user})
#         assert validity == serializer.is_valid(raise_exception=True)
#
#     except Exception as e:
#         print(e)
#         assert not validity
#
