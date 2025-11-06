import json
from rich.console import Console
from rich.table import Table

with open('countries_data.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)

console = Console()

# e
english_countries = []
total_english_population = 0

for country in countries:
    if 'languages' in country and any('english' in lang.lower() for lang in country['languages']):
        english_countries.append(country)
        total_english_population += country.get('population', 0)

top_english = sorted(english_countries, key=lambda x: x.get('population', 0), reverse=True)[:10]
table_e = Table(title="10 країн з найбільшим населенням (англомовні)")
table_e.add_column("Країна", style="cyan")
table_e.add_column("Столиця", style="magenta")
table_e.add_column("Населення", style="green")

for country in top_english:
    table_e.add_row(
        country.get('name', 'N/A'),
        country.get('capital', 'N/A'),
        f"{country.get('population', 0):,}"
    )

console.print(table_e)
console.print(f"Сумарне населення англомовних країн: {total_english_population:,}\n")

# c
euro_countries = []
total_euro_population = 0

for country in countries:
    if 'currencies' in country and any('eur' in curr.get('code', '').lower() for curr in country['currencies']):
        euro_countries.append(country)
        total_euro_population += country.get('population', 0)

table_c = Table(title="Країни з валютою Євро")
table_c.add_column("Країна", style="cyan")
table_c.add_column("Столиця", style="magenta")
table_c.add_column("Населення", style="green")

for country in euro_countries:
    table_c.add_row(
        country.get('name', 'N/A'),
        country.get('capital', 'N/A'),
        f"{country.get('population', 0):,}"
    )
console.print(table_c)
console.print(f"Сумарне населення країн з євро: {total_euro_population:,}")