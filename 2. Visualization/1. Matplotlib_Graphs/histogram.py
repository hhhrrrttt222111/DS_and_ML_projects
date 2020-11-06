import matplotlib.pyplot as plt
import pandas as pd


# ages = [18, 19, 21, 25, 26, 30, 32, 38, 45, 60]
data = pd.read_csv('./data/age.csv')
ages = data['Age']
ids = data['Responder_id']

median_age = 29
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, edgecolor='black', log=True)

plt.axvline(median_age, color='red', label='Age Media')

plt.legend()
plt.title('HISTOGRAM')
plt.xlabel('Ages')
plt.ylabel('Salaries')

plt.tight_layout()
plt.show()
