def test_failed_login_count():
    failed_logins = {}

    username = "Mike"

    if username not in failed_logins:
        failed_logins[username] = 0

    failed_logins[username] += 1

    assert failed_logins["Mike"] == 1
def test_brute_force_detection():
    failed_attempts = 4

    assert failed_attempts >= 3    

def get_severity(attempts):
    if attempts >= 3:
        return "HIGH"
    elif attempts == 2:
        return "MEDIUM"
    else:
        return "LOW"


def test_security_severity():
    assert get_severity(1) == "LOW"
    assert get_severity(2) == "MEDIUM"
    assert get_severity(4) == "HIGH"