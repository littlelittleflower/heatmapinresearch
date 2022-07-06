import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import numpy as np


data_cwjt = pandas.read_excel('heatmap_cwjt.xls',index_col=0)
data_cnn = pandas.read_excel('heatmap_cnn.xls',index_col=0)


cmax = np.max([data_cnn, data_cwjt])
cmin = 0


fig = plt.figure(1, figsize=(12, 6))

ax1 = fig.add_subplot(1, 2, 1)
heatmap_cnn = sns.heatmap(data=data_cnn, cmap='YlOrRd',vmin=cmin, vmax=cmax,cbar=False)
heatmap_cnn.set_xticklabels(heatmap_cnn.get_xticklabels(), rotation=0)
plt.xlabel('Baseline model predict result',fontsize=10, color='k')
plt.ylabel('True labels',fontsize=10, color='k')
foo_fig = plt.gcf() # 'get current figure'
cbar = heatmap_cnn.collections[0].colorbar
# cbar.set_label('error density')


#,cbar_kws = dict(use_gridspec=False,location="top")
ax2 = fig.add_subplot(1, 2, 2)
heatmap_cwjt = sns.heatmap(data=data_cwjt, cmap='YlOrRd',vmin=cmin, vmax=cmax)
heatmap_cwjt.set_xticklabels(heatmap_cwjt.get_xticklabels(), rotation=0)
plt.xlabel('CWT-Joint model predict result',fontsize=10, color='k')
plt.ylabel('True labels',fontsize=10, color='k')
foo_fig = plt.gcf() # 'get current figure'
cbar = heatmap_cwjt.collections[0].colorbar
cbar.set_label('error density')




foo_fig.savefig('heatmap.png', format='png', dpi=1000)
foo_fig.savefig('heatmap.eps', format='eps', dpi=1000)
plt.show()