%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


df=pd.read_csv('/storage/emulated/0/Download/epa-sea-level.csv')


    # Read data from file

def draw_plot():
    # Create scatter plot
    fig=plt.figure(figsize=(10,5))
    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level')
  

    # Create first line of best fit
    
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']

    res1=linregress(x,y)
    x1=pd.Series(range(1880,2051))
    y1=res1.intercept + res1.slope*x1
    plt.plot(x1,y1,'r',label='fit:1880-2050')
    


    # Create second line of best fit
    
    recent=df[df['Year']>=2000]
    res2=linregress(recent['Year'],
                recent['CSIRO Adjusted Sea Level'])

    x3=pd.Series(range(2000,2051))
    y3=res2.intercept+res2.slope*x3
    plt.plot(x3,y3,'blue')
    

    # Add labels and title
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level')
    plt.legend()
    plt.grid(True)

    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return fig