import pandas as pd
from datetime import datetime


nba = pd.read_csv('nba_players.csv', parse_dates=['Birthday'])
team_data = nba[nba['Team'] == 'Denver Nuggets'].copy()
current_year = pd.Timestamp.now().year
team_data['Age'] = current_year - team_data['Birthday'].dt.year

# 1
print("1. Гравці команди Denver Nuggets (сортовано за ім'ям):")
print(team_data.sort_values('Name').to_string(index=False))

# 2
print(f"\n2. Кількість гравців в команді: {len(team_data)}")

# 3
print("\n3. Кількість гравців на позиціях:")
print(team_data['Position'].value_counts().to_string())

# 4
print("\n4. 3 наймолодші гравці:")
print(team_data.nsmallest(3, 'Age')[['Name', 'Age']].to_string(index=False))
print("\n4. 3 найстарші гравці:")
print(team_data.nlargest(3, 'Age')[['Name', 'Age']].to_string(index=False))

# 5
print("\n5. 3 гравці з найменшою зарплатою:")
print(team_data.nsmallest(3, 'Salary')[['Name', 'Salary']].to_string(index=False))
print("\n5. 3 гравці з найбільшою зарплатою:")
print(team_data.nlargest(3, 'Salary')[['Name', 'Salary']].to_string(index=False))

# 6
print("\n6. Середні зарплати на позиціях:")
print(team_data.groupby('Position')['Salary'].mean().round(0).to_string())

# 7
print("\n7. Гравці на позиції PF (відсортовані за віком):")
pf_players = team_data[team_data['Position'] == 'PF'].sort_values('Age')
print(pf_players[['Name', 'Age', 'Salary']].to_string(index=False) if not pf_players.empty else "Немає гравців на позиції PF")

# 8
print(f"\n8. Середня зарплата: ${team_data['Salary'].mean():.0f}")
print(f"8. Медіанна зарплата: ${team_data['Salary'].median():.0f}")

# 9
print(f"\n9. Середній вік гравців: {team_data['Age'].mean():.1f} років")

# 10
print("\n10. Гравці з зарплатою менше $2 млн:")
low_salary = team_data[team_data['Salary'] < 2_000_000]
print(low_salary[['Name', 'Salary']].to_string(index=False) if not low_salary.empty else "Немає таких гравців")

# 11
avg_salary = team_data['Salary'].mean()
print(f"\n11. Гравці з зарплатою вище середньої (${avg_salary:.0f}):")
above_avg = team_data[team_data['Salary'] > avg_salary]
print(above_avg[['Name', 'Salary']].to_string(index=False))

# 12
print("\n12. Гравці, які народилися в 1990-1995 роках:")
born_1990_1995 = team_data[(team_data['Birthday'].dt.year >= 1990) & (team_data['Birthday'].dt.year <= 1995)]
print(born_1990_1995[['Name', 'Birthday']].to_string(index=False) if not born_1990_1995.empty else "Немає таких гравців")