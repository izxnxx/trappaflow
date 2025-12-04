import hashlib
import requests
import time

class VirusTotalAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base = 'https://www.virustotal.com/api/v3/'
        self.headers = {'x-apikey': api_key}

    def _hash(self, path):
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def check_file_report(self, path):
        hash_val = self._hash(path)
        url = f"{self.base}files/{hash_val}"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 200:
            return True, resp.json()
        return False, None

    def upload_file(self, path):
        with open(path, 'rb') as f:
            files = {'file': (path, f)}
            resp = requests.post(self.base + 'files', headers=self.headers, files=files)
            return resp.json()['data']['id']

    def get_scan_report(self, hash_val):
        url = f"{self.base}files/{hash_val}"
        return requests.get(url, headers=self.headers).json()

    def print_scan_report(self, report):
        stats = report['data']['attributes']['last_analysis_stats']
        print("\nСтатистика:")
        for k, v in stats.items():
            print(f"{k}: {v}")

        results = report['data']['attributes']['last_analysis_results']
        print("\nПозитивні виявлення:")
        for av, res in results.items():
            if res['category'] in ['malicious', 'suspicious']:
                print(f"{av}: {res['result']}")

    def analyze_report(self, analysis_id):
        for _ in range(30):
            resp = requests.get(self.base + f'analyses/{analysis_id}', headers=self.headers)
            if resp.json()['data']['attributes']['status'] == 'completed':
                return True
            time.sleep(10)
        return False



vt = VirusTotalAPI("ВАШ_КЛЮЧ")
file_path = "test.exe"
exists, report = vt.check_file_report(file_path)
if exists:
    vt.print_scan_report(report)
else:
    aid = vt.upload_file(file_path)
    if vt.analyze_report(aid):
        report = vt.get_scan_report(vt._hash(file_path))
        vt.print_scan_report(report)