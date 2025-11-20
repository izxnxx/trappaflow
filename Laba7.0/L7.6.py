import json
from typing import Dict, List


def suspicious_by_laddr(entry: Dict) -> bool:
    return "laddr" in entry and bool(entry["laddr"])


def suspicious_by_laddr_raddr(entry: Dict) -> bool:
    return ("laddr" in entry and bool(entry["laddr"]) and
            "raddr" in entry and bool(entry["raddr"]))


def get_suspicious_pids(filename: str) -> List[int]:
    pids_laddr: List[int] = []
    pids_laddr_raddr: List[int] = []

    with open(filename, "r", encoding="utf-8") as f:
        logs = json.load(f)

    for entry in logs:
        pid = entry.get("pid")
        if isinstance(pid, int):
            # Перевіряємо connections, а не сам entry
            connections = entry.get("connections", [])
            for conn in connections:
                if suspicious_by_laddr(conn):
                    pids_laddr.append(pid)
                if suspicious_by_laddr_raddr(conn):
                    pids_laddr_raddr.append(pid)

    print("PID з laddr:", sorted(set(pids_laddr)))
    print("PID з laddr та raddr:", sorted(set(pids_laddr_raddr)))

    return sorted(set(pids_laddr_raddr))


if __name__ == "__main__":
    suspicious_pids = get_suspicious_pids("system_logs.json")
    print("Підозрілі PID процесів:", suspicious_pids)