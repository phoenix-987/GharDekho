# import pytest
# from authorization.models import User
# from django.db.transaction import atomic
#
#
# @pytest.mark.django_db
# # Parameterize marker to test the cases.
# @pytest.mark.parametrize(
#     'email, name, password, is_owner, validity',
#     [
#         ('test@test.com', 'test', 'password', True, True),             # Test case with all data::RESULT-TRUE
#         (None, 'Nathan', 'password', True, False),                     # Test case with no email address::RESULT-FALSE
#         ('abc@example.com', None, 'password', False, False),           # Test case with no name value::RESULT-FALSE
#         ('Krishna@example.com', 'Krishna', None, False, True),         # Test case with no password::RESULT-TRUE
#         ('Krishna@example.com', 'Krishna', 'password', None, False),   # Test case with no is_owner status::RESULT-FALSE
#     ]
# )
# # Test for creating user with different case like all values, None values.
# def test_create_user(email, name, password, is_owner, validity):
#     try:
#         # Creating user with atomic so that it will not give TransactionManagementError (violates not null constraint).
#         with atomic():
#             User.objects.create_user(email=email, name=name, password=password, is_owner=is_owner)
#
#         # Counting and asserting the validity that user has been created or not.
#         count = User.objects.all().count()
#         assert count == validity
#
#     except Exception as e:
#         print(e)
#         assert not validity
#
