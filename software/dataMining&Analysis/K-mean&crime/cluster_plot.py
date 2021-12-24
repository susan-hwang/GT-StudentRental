import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import pandas as pd

# from matplotlib.backends.backend_pdf import PdfPages


# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

df = pd.read_csv('rentalList_Time_crime_score.csv')
res = np.array(df[['Latitude', 'Longitude', 'clusters']])

color=iter(cm.rainbow(np.linspace(0,1,10)))


for i in range(10):
	idx = np.where(res[:, 2] == i)
	x = res[idx, 0]
	y = res[idx, 1]
	cc = next(color)
	plt.scatter(x, y, s = 60, c = cc, alpha = 0.5)

plt.show()
plt.close()