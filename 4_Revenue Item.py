import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'AppleGothic'

data = pd.read_csv('예산편성현황(총액).csv')
data['정부안금액(천원)'] = data['정부안금액(천원)'].str.replace(',', '').astype(int)

plt.figure(figsize=(7, 5))

sub_data = data[
    (data['소관명'] == '기획재정부') &
    (data['수입관명'] == '내국세')
]

sub_finance_data = (
    sub_data
    .groupby('수입항명')['정부안금액(천원)']
    .sum().sort_values(ascending=False)
    .head(5)
)

plt.title('Budget Composition by Revenue Item of Domestic Taxes in Ministry of Strategy and Finance')
plt.xlabel('Budget Amount')
plt.ylabel('Revenue Item')

plt.barh(y=sub_finance_data.index, width=sub_finance_data.values)

plt.show()