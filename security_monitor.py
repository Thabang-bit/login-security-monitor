import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--log-file", default="logs.txt")
args = parser.parse_args()

failed_logins = {}
failed_ips = {}
suspicious_ips = []
failed_login_times = []

total_logins = 0
successful_logins = 0


with open("logs.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        date = parts[0]
        time = parts[1]
        username = parts[2]
        ipaddress = parts[3]
        status = parts[4]
        total_logins += 1

        if status == "SUCCESS":
            successful_logins += 1

        if status == "FAILED":
            if username not in failed_logins:
                failed_logins[username] = 0

            failed_logins[username] += 1

            if ipaddress not in failed_ips:
                failed_ips[ipaddress] = 0

            failed_ips[ipaddress] += 1
            failed_login_times.append(f"{date} {time} - {username} - {ipaddress}")

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

    print("\n===== IP ADDRESS REPORT =====")
    report.write("\n===== IP ADDRESS REPORT =====\n")

    for ipaddress, attempts in failed_ips.items():
        message = f"{ipaddress}: {attempts} failed login attempts"
        print(message)
        report.write(message + "\n")

        if attempts >= 3:
            severity = "HIGH"
            warning = f"WARNING: {ipaddress} may be under a brute-force attack!"
            print(warning)
            print(f"Severity: {severity}")
            report.write(warning + "\n")
            report.write(f"Severity: {severity}\n")
            suspicious_ips.append(ipaddress)

        elif attempts == 2:
            severity = "MEDIUM"
            print(f"Severity: {severity}")
            report.write(f"Severity: {severity}\n")

        else:
            severity = "LOW"
            print(f"Severity: {severity}")
            report.write(f"Severity: {severity}\n")    

    print("\n===== SUSPICIOUS IP ADDRESSES =====")
    report.write("\n===== SUSPICIOUS IP ADDRESSES =====\n")

    for ipaddress in suspicious_ips:
        print(ipaddress)
        report.write(ipaddress + "\n")

        total_failed_attempts = sum(failed_ips.values())

        print("\n===== SECURITY SUMMARY =====")
        print(f"Total failed login attempts: {total_failed_attempts}")
        print(f"Successful logins: {successful_logins}")
        print(f"Failed login attempts: {total_failed_attempts}")
        print(f"Suspicious IP addresses: {len(suspicious_ips)}")

        report.write("\n===== SECURITY SUMMARY =====\n")
        report.write(f"Total failed login attempts: {total_failed_attempts}\n")
        report.write(f"Successful logins: {successful_logins}\n")
        report.write(f"Failed login attempts: {total_failed_attempts}\n")
        report.write(f"Suspicious IP addresses: {len(suspicious_ips)}\n")

        print("\n===== FAILED LOGIN TIMES =====")
        report.write("\n===== FAILED LOGIN TIMES =====\n")

        for login in failed_login_times:
            print(login)
            report.write(login + "\n")        

with open("security_report.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["IP Address", "Failed Attempts", "Severity"])

    for ipaddress, attempts in failed_ips.items():
        if attempts >= 3:
            severity = "HIGH"
        elif attempts == 2:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        writer.writerow([ipaddress, attempts, severity])