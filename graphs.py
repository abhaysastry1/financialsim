import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
from portfolio.userInput import askVals
from portfolio.simplePortfolio import getYearlyPortfolio
from portfolio.simplePortfolio import getYears


results = askVals()
a = getYears()
b = getYearlyPortfolio()

data1 = {'Year': a,
         'Portfolio Value': b
        }
df2 = DataFrame(data1,columns=['Year','Portfolio Value'])
print (df2)

root = tk.Tk()
figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Portfolio Value']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Portfolio Value')

root.mainloop()
