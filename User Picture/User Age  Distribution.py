import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(dpi=200, figsize=(8, 8))
Num = 44048
data = [394, 5352, 13891, 13848, 8411, 2152]
labels = ['<18', '18-25', '26-35', '36-45', '46-60', '>60']
colors = plt.get_cmap('Blues')(np.linspace(0.1, 0.6, len(labels)))
sizes = [data[0] / Num * 100, data[1] / Num * 100, data[2] / Num * 100, data[3] / Num * 100, data[4] / Num * 100,
         data[5] / Num * 100]
expodes = (0, 0, 0.15, 0, 0, 0)
plt.pie(sizes, startangle=120, explode=expodes, labels=labels, shadow=True, colors=colors, autopct='%10.1f%%', textprops={'fontsize': 15}, labeldistance=1.05, pctdistance=0.6)
plt.axis('equal')
plt.title('User Age Distribution', fontsize=30)
plt.savefig('./User Age Distribution.png')
plt.show()
