import numpy as np
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
    def __init__(self, thres=0.01, other="other", enc=OneHotEncoder()):
        """

        :type enc: encoder (just one-hot)
        """
        self.thres = thres
        self.other = other
        self.encoder = enc

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        vc = X.value_counts()
        crit = (vc / vc.sum()).lt(self.thres)
        X = np.array(np.where(X.isin(vc[crit].index), self.other, X))
        X = self.encoder.fit_transform(X.reshape(-1, 1))
        return X


class OrdinalLumper(BaseEstimator, TransformerMixin):
    def __init__(self, thres=0.01, other="other"):
        self.thres = thres
        self.other = other

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        vc = X.value_counts()
        crit = (vc / vc.sum()).lt(self.thres)
        X = np.array(np.where(X.isin(vc[crit].index), self.other, X))
        vc2 = pd.Series(X).value_counts()
        c_order = vc2.index.values.tolist()
        if self.other in c_order:
            c_order.sort(key=self.other.__eq__)
        c_order = [np.array(c_order)]
        X = OrdinalEncoder(categories=c_order).fit_transform(X.reshape(-1, 1))
        return X
