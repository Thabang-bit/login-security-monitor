def test_failed_login_count():
    failed_logins = {}

    username = "Mike"

    if username not in failed_logins:
        failed_logins[username] = 0

    failed_logins[username] += 1

    assert failed_logins["Mike"] == 1