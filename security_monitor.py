failed_logins = {}

with open("logs.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        date = parts[0]
        time = parts[1]
        username = parts[2]
        status = parts[3]

        if status == "FAILED":
            if username not in failed_logins:
                failed_logins[username] = 0

            failed_logins[username] += 1

print("===== SECURITY REPORT =====")

with open("report.txt", "w") as report:
    report.write("===== SECURITY REPORT =====\n\n")

    for username, attempts in failed_logins.items():
        message = f"{username}: {attempts} failed login attempts"
        print(message)
        report.write(message + "\n")

        if attempts >= 3:
            warning = f"WARNING: {username} may be under a brute-force attack!"
            print(warning)
            report.write(warning + "\n")