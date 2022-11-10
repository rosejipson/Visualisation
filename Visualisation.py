# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:57:23 2022

@author: RJ
"""

# import pandas library
import pandas as pd
import matplotlib.pyplot as plt

# reading data  from csv file for plotting line, bar and bar stacking plot
adr = pd.read_excel("Age_Dependancy ratio.xlsx")

def line():
    """This function is used to plot a line graph of Age Dependency Ratio."""
    
    adr1 = adr[2:10]
    plt.figure()
    plt.plot(adr1['Country Name'], adr1[2000], label="2000")
    plt.plot(adr1['Country Name'], adr1[2005], label="2005")
    plt.plot(adr1['Country Name'], adr1[2010], label="2010")
    plt.plot(adr1['Country Name'], adr1[2015], label="2015")

    plt.title("Age Dependency Ratio")
    plt.xlabel("Country")
    plt.xticks(rotation = 90)
    plt.ylabel("ADR (% of working-age population)")
    plt.legend(fontsize=8)
    plt.savefig("Lineplot.png",bbox_inches = "tight")
    plt.show()
line()    


def bar():
    """This function is used to plot a bar graph of Age Dependency Ratio."""
    
    adr2 = adr[11:20]
    plt.figure()
    plt.bar(adr2['Country Name'], adr2[2021], label="2021", width=0.5)
    plt.xticks(rotation = 90)
    plt.xlabel("Country")
    plt.ylabel("ADR (% of working-age population)")
    plt.title("Age Dependency Ratio")
    plt.legend(fontsize = 7)
    plt.savefig("Bargraph.png",bbox_inches="tight")
    plt.show()
bar()
    
def barstack():
    """This function is used to plot a barstack graph of Age Dependency Ratio."""
    
    adr3 = adr[10:20]
    plt.figure()
    plt.bar(adr3['Country Name'], adr3[1990],width=0.3, label="1990", color = "Red", alpha = 0.5)
    plt.bar(adr3['Country Name'], adr3[2000],width=0.3, label="2000", color = "Blue", alpha = 0.5)
    
    plt.title("Age Dependency Ratio")
    plt.xticks(rotation = 90)
    plt.xlabel("Country")
    plt.ylabel("ADR (% of working-age population)")
    plt.legend(fontsize=7)
    plt.savefig("Stackingbar.png",bbox_inches="tight")
    plt.show()
barstack()




