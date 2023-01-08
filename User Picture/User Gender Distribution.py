import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(dpi=200, figsize=(8, 8))
Num = 44109
data = [18590, 25422, 97]
labels = ['Male', 'Female', 'Unknown']
colors = plt.get_cmap('Greens')(np.linspace(0.1, 0.6, len(labels)))
sizes = [data[0] / Num * 100, data[1] / Num * 100, data[2] / Num * 100]
expodes = (0.15, 0, 0)
plt.pie(sizes, startangle=60, explode=expodes, labels=labels, shadow=True, colors=colors, autopct='%10.1f%%', textprops={'fontsize': 15}, labeldistance=1.05, pctdistance=0.6)
plt.axis('equal')
plt.title('User Gender Distribution', fontsize=30)
plt.savefig('./User Gender Distribution.png')
plt.show()
