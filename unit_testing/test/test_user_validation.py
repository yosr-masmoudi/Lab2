


from unit_testing.src.user_validation import is_valid_username, is_valid_password, is_valid_email
 
 
def test_valid_username():
    assert is_valid_username("user123") is True
    assert is_valid_username("") is False
    assert is_valid_username("user name") is False
 
 
def test_valid_password():
    assert is_valid_password("Password1!") is True
    assert is_valid_password("short1!") is False
    assert is_valid_password("NoSpecialChar1") is False
    assert is_valid_password("NoNumber!") is False
    assert is_valid_password("nonumberorspecial") is False
 
 
def test_valid_email():
    assert is_valid_email("user@example.com") is True
    assert is_valid_email("userexample.com") is False
    assert is_valid_email("user@com") is False
    assert is_valid_email("") is False