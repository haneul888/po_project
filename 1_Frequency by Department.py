import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Korean font
rcParams['font.family'] = 'AppleGothic'


data = pd.read_csv('예산편성현황(총액).csv')

institution_counts = data['소관명'].value_counts(ascending=False)[:5]

plt.title('Frequency by Department')
plt.xlabel('Frequency')
plt.ylabel('Department')

plt.barh(y=institution_counts.index, width=institution_counts.values)

plt.show()


