import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'AppleGothic'

data = pd.read_csv('예산편성현황(총액).csv')
data['정부안금액(천원)'] = data['정부안금액(천원)'].str.replace(',', '').astype(int)

# Top 5
grouped_data = (
    data
    .groupby('소관명')['정부안금액(천원)']
    .sum().sort_values(ascending=False)
    .head(5)
)

# Reducing Units
scaled_values = grouped_data / 100_000_000

plt.figure(figsize=(10,6))
plt.barh(y=scaled_values.index, width=scaled_values.values, color='skyblue')
plt.title('Top 5 Departments by Budget Received')
plt.xlabel('Budget Amount (100 million KRW)')
plt.ylabel('Department')

plt.show()
