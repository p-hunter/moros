
import numpy as np
from spectrum import *
import pandas as pd


def which_max(x):
    x.index(max(x))

def spec_yw(x,o):
    x_acf = acf(x, nlags = o)
    if x_acf[0] == 0:
        print("Zero Variance Found")
        return(0)
    
    return

def find_frequency(x):
    n = len(x)    
    print("\nLength of x: {}\n".format(n))    
    trend = np.linspace(1, n, n).reshape(-1, 1)    
    print("\nTime Trend Aquired\n")    
    m = LinearRegression().fit(trend, x)    
    print("\n Linear Model Fitted\n")    
    # remove time trend from x
    x = m.predict(trend) - x        
    print("\nTime Trend Stripped from x\n")
    print(x)
    o = min([n - 1, math.floor(10 * math.log10(n))])
    print("\nOrder of data: {}\n".format(o))
    n_freq = 500
    spec = pyule(x, order = o, NFFT = n_freq)
    print("\nSpectral YW Mod Ran\n")
    spec_df = pd.DataFrame({
        "PSD" : spec.psd,
        "Freq" : spec.frequencies()        
        })   
    p = spec_df.loc[spec_df.PSD == max(spec_df.PSD),"Freq"].values
    p = int(np.floor(1 / p))
    return(p)
    if max(spec.PSD) > 10:        
        p = spec_df.loc[spec_df.PSD == max(spec_df.PSD),"Freq"].values
        p = int(np.floor(1 / p))
        if p == math.inf:
            print("\nPeriod is Infinite... correcting...\n")
            spec_df = spec_df[spec_df.PSD < np.inf]
            p = spec_df.loc[spec_df.PSD == max(spec_df.PSD),"Freq"].values
            p = int(np.floor(1 / p))
        else:
            p = 1
    else:
        p = 1
    p = int(p)
    return(p)
                                                         
            
