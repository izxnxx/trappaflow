import csv
from collections import defaultdict
from rich.console import Console
from rich.table import Table

with open('log_file_8.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    logs = list(reader)

console = Console()

user_fails = defaultdict(int)
user_logs = defaultdict(list)

for user, time, ip, status in logs:
    user_logs[user].append([user, time, ip, status])
    if status == 'fail':
        user_fails[user] += 1

suspicious_users = {user: user_fails[user] for user in user_fails if user_fails[user] >= 6}

table_a = Table(title="Користувачі з ≥6 невдалих спроб")
table_a.add_column("Користувач", style="cyan")
table_a.add_column("Невдалих спроб", style="red")

for user, count in suspicious_users.items():
    table_a.add_row(user, str(count))

console.print(table_a)

for user in suspicious_users:
    table_logs = Table(title=f"Логи користувача {user}")
    table_logs.add_column("Користувач")
    table_logs.add_column("Час")
    table_logs.add_column("IP")
    table_logs.add_column("Статус")

    for log in user_logs[user]:
        table_logs.add_row(*log)

    console.print(table_logs)

ip_accounts = defaultdict(set)
ip_logs = defaultdict(list)

for user, time, ip, status in logs:
    ip_accounts[ip].add(user)
    ip_logs[ip].append([user, time, ip, status])

suspicious_ips = {ip: len(ip_accounts[ip]) for ip in ip_accounts if len(ip_accounts[ip]) >= 3}

table_b = Table(title="IP-адреси з входами в ≥3 акаунтів")
table_b.add_column("IP-адреса", style="magenta")
table_b.add_column("Кількість акаунтів", style="green")

for ip, count in suspicious_ips.items():
    table_b.add_row(ip, str(count))

console.print(table_b)

for ip in suspicious_ips:
    table_ip_logs = Table(title=f"Логи IP {ip}")
    table_ip_logs.add_column("Користувач")
    table_ip_logs.add_column("Час")
    table_ip_logs.add_column("IP")
    table_ip_logs.add_column("Статус")

    for log in ip_logs[ip]:
        table_ip_logs.add_row(*log)

    console.print(table_ip_logs)