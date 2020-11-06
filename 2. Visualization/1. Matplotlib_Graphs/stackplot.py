import matplotlib.pyplot as plt


plt.style.use('seaborn')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [1, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#90EE90', '#00FF00', '#3CB371']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)
plt.legend(loc=(0.07, 0.05))


plt.title('Stack Plot')
plt.tight_layout()
plt.show()

