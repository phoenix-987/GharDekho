import pytest
from authorization.serializers import SendResetPwdMailSerializer


# Parameterize marker to test the cases.
@pytest.mark.parametrize(
    "email, validity",
    [
        (None, False),                      # Test case with no data::RESULT-FALSE
        ("naman.j@com", False),             # Test case with all incorrect domain::RESULT-FALSE
        ("naman.j.com", False),             # Test case with no address::RESULT-FALSE
        ("test@test.com", False),           # Test case with unregistered mail id::RESULT-FALSE
        ("s.kir001990@gmail.com", True),    # Test case with registered email id::RESULT-TRUE
    ]
)
def test_send_reset_pwd_mail_serializer(db, create_dummy_user, email, validity):
    try:
        # Testing Serializer by calling with required value.
        serializer = SendResetPwdMailSerializer(data={"email": email})
        assert validity == serializer.is_valid(raise_exception=True)

    except Exception as e:
        assert not validity
