import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder

class Lumper(BaseEstimator, TransformerMixin):
    def __init__(self, thres=0.01, other="other"):
        self.thres = thres
        self.other = other    

    def fit(self, X, y=None):
        return(self)

    def transform(self, X, y=None):
        vc = X.value_counts()
        crit = (vc/vc.sum()).lt(self.thres)
        X = np.array(np.where(X.isin(vc[crit].index), self.other, X))
        X = OneHotEncoder().fit_transform(X)
        return(X)
