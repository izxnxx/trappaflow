import pandas as pd

df = pd.read_csv('Fortune 500 Companies_2023.csv')

print(f"Кількість компаній: {len(df)}")


print("\na. Найгірші 10 компаній за активами:")
worst_assets = df.nsmallest(10, 'asset_mil')
for _, row in worst_assets.iterrows():
    print(f"Ранг {row['rank']}: {row['name']} - Активи: {row['asset_mil']:,.0f} млн")

print("\nb. Найкращі 10 компаній за співвідношенням дохід/активи:")
df['revenue_to_assets'] = df['revenue_mil'] / df['asset_mil']
best_ratio = df.nlargest(10, 'revenue_to_assets')
for _, row in best_ratio.iterrows():
    print(f"Ранг {row['rank']}: {row['name']} - Співвідношення: {row['revenue_to_assets']:.2f}")

