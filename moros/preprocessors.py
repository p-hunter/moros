import numpy as np
import scipy.stats as stats
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

class Lumper(BaseEstimator, TransformerMixin):
    def __init__(self, thres=0.01, other = "other", enc = OneHotEncoder()):
        self.thres = thres
        self.other = other
        self.encoder = enc

    def fit(self, X, y=None):
        return(self)

    def transform(self, X, y=None):
        vc = X.value_counts()
        crit = (vc/vc.sum()).lt(self.thres)
        X = np.array(np.where(X.isin(vc[crit].index), self.other, X))
        X = self.encoder.fit_transform(X)
        return X
class OneHotLumper(BaseEstimator, TransformerMixin):
    def __init__(self, thres=0.01, other = "other"):
        self.thres = thres
        self.other = other
        self.encoder = OneHotEncoder()

    def fit(self, X, y=None):
        return(self)

    def transform(self, X, y=None):
        vc = X.value_counts()
        crit = (vc/vc.sum()).lt(self.thres)
        X = np.array(np.where(X.isin(vc[crit].index), self.other, X))
        X = self.encoder.fit_transform(X.reshape(-1, 1))
        return(X)
    
class OrdinalLumper(BaseEstimator, TransformerMixin):
    def __init__(self, thres=0.01, other = "other"):
        self.thres = thres
        self.other = other        

    def fit(self, X, y=None):
        return(self)

    def transform(self, X, y=None):
        vc = pd.DataFrame(X).value_counts()
        crit = (vc/vc.sum()).lt(self.thres)
        X = np.array(np.where(pd.DataFrame(X).isin(vc[crit].index), self.other, X))
        vc2 = pd.DataFrame(X).value_counts()
        c_order = vc2.index.values.tolist()
        if self.other in c_order:
            c_order.sort(key=self.other.__eq__)
        c_order = [np.array(pd.DataFrame(X).iloc[:,0].value_counts().index.values.tolist())]
        X = OrdinalEncoder(categories=c_order).fit_transform(X.reshape(-1, 1))
        return(X)
    

class log10_uniform(): 
    def __init__(self, a=-1, b=0):
        self.loc = a
        self.scale = b - a        

    def rvs(self, size: int=None, random_state=None):
        uniform = stats.uniform(loc=self.loc, scale=self.scale)
        if size is None:
            return np.power(10, uniform.rvs(random_state=random_state))
        else:
            return np.power(10, uniform.rvs(size=size, random_state=random_state))