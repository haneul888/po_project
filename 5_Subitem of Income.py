import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'AppleGothic'

data = pd.read_csv('예산편성현황(총액).csv')
data['정부안금액(천원)'] = data['정부안금액(천원)'].str.replace(',', '').astype(int)

plt.figure(figsize=(7, 5))

income_tax_data = data[
    (data['소관명'] == '기획재정부') &
    (data['수입관명'] == '내국세') &
    (data['수입항명'] == '소득세')
]

income_tax_detail = (
    income_tax_data
    .groupby('수입목명')['정부안금액(천원)']
    .sum().sort_values(ascending=False)
)

plt.title('Budget Composition by Subitem of Income Tax in Domestic Taxes of Ministry of Strategy and Finance')
plt.xlabel('Budget Amount')
plt.ylabel('Subitem of Revenue')

plt.barh(y=income_tax_detail.index, width=income_tax_detail.values)
plt.show()