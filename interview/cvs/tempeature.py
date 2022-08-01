import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    tempeature = np.random.normal(20,2,31)
    temp_date = pd.date_range(start='5/01/2022', end='5/31/2022') 
    df = pd.DataFrame({'tempeature':tempeature,'date':temp_date})
    df['tempeature'].plot()
    plt.show()
    print(df)
    
       