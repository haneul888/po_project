import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'AppleGothic'

data = pd.read_csv('예산편성현황(총액).csv')
data['정부안금액(천원)'] = data['정부안금액(천원)'].str.replace(',', '').astype(int)

plt.figure(figsize=(7,5))

finance_data = (
    data[data['소관명'] == '기획재정부']
    .groupby('수입관명')['정부안금액(천원)']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.title('Budget Composition by Revenue Category in Ministry of Strategy and Finance')
plt.xlabel('Budget Amount')
plt.ylabel('Revenue Category')

plt.barh(y=finance_data.index, width=finance_data.values)
plt.show()