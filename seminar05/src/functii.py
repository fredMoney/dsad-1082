import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from scipy.stats import entropy

def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]): # -> daca coloana e numerica
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True) # -> in cazul non-numeric valorile nan se inlocuiesc cu modulul


def f_disimilaritate(t):
    assert isinstance(t, pd.DataFrame)
    x = t.iloc[:, :-1].values
    s = np.sum(x, axis=1)
    r = (s - x.T).T
    tx = np.sum(x, axis=0)
    tr = np.sum(r, axis=0)
    tx[tx==0] = 1
    tr[tr==0] = 1
    d = 0.5 * np.sum(np.abs(x/tx - r/tr), axis=0)
    return pd.Series(d, t.columns[:-1])

def f_shannon(t):
    assert isinstance(t, pd.DataFrame)
    x = t.iloc[:, :-1].values
    tx = np.sum(x, axis=0) # axis=0 -> calcul pe coloana
    tx[tx==0] = 1
    p = x/tx
    p[p==0] = 1
    h = entropy(p, axis=0, base=2)
    return pd.Series(h, t.columns[:-1])