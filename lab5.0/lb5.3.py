from rich.console import Console
from rich.table import Table

console = Console()

logs = []
with open('log_file_8.csv', 'r') as file:
    headers = file.readline()
    for line in file:
        user, time, ip, status = line.strip().split(',')
        logs.append([user, time, ip, status])

print(f"Завантажено {len(logs)} записів")
print("\nА. КОРИСТУВАЧІ З 6+ НЕВДАЛИХ СПРОБ")

failed_count = {}
for user, _, _, status in logs:
    if status == 'fail':
        failed_count[user] = failed_count.get(user, 0) + 1

suspicious_users = {user: count for user, count in failed_count.items() if count >= 6}
print(f"Знайдено: {len(suspicious_users)}")

for user, count in suspicious_users.items():
    table = Table(title=f"{user} ({count} невдалих спроб)")
    table.add_column("Час")
    table.add_column("IP")
    table.add_column("Статус")

    for log in logs:
        if log[0] == user and log[3] == 'fail':
            table.add_row(log[1], log[2], log[3])
    console.print(table)
print("\nБ. IP-АДРЕСИ З ВХОДАМИ В 3+ АКАУНТІВ")

ip_accounts = {}
for user, _, ip, status in logs:
    if status == 'success':
        if ip not in ip_accounts:
            ip_accounts[ip] = set()
        ip_accounts[ip].add(user)

suspicious_ips = {ip: users for ip, users in ip_accounts.items() if len(users) >= 3}
print(f"Знайдено: {len(suspicious_ips)}")

for ip, users in suspicious_ips.items():
    table = Table(title=f"{ip} ({len(users)} акаунтів)")
    table.add_column("Користувач")
    table.add_column("Час")
    table.add_column("Статус")

    for log in logs:
        if log[2] == ip and log[3] == 'success':
            table.add_row(log[0], log[1], log[3])
    console.print(table)