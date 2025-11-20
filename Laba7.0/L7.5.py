import requests

def check_ip_country(ip_list: list[str]) -> list[str]:
    
    countries = []
    for ip in ip_list:
        try:
            url = f"https://ipinfo.io/{ip}/json"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                country = data.get("country", "Unknown")
                countries.append(country)
            else:
                countries.append("Unknown")
        except Exception:
            countries.append("Unknown")
    return countries

ip_addresses = ['46.166.139.111', '2.132.242.55', '110.227.199.106', '117.50.3.28', '104.131.30.14']
result = check_ip_country(ip_addresses)
print(result)
