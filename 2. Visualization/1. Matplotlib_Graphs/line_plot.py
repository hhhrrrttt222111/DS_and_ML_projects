import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('./data/data1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


plt.plot(ages, dev_salaries, color='#00FF00', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

overall_median = 57000

plt.fill_between(ages, py_salaries, dev_salaries, alpha=0.25,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, label='Above Avg:')
plt.fill_between(ages, py_salaries, dev_salaries, alpha=0.25,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', label='Below Avg:')


plt.title('LinePlot')
plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.tight_layout()
plt.show()
