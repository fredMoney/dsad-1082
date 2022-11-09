import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def nan_replace_t(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

def tabelare_varianta(alpha):
    return pd.DataFrame(
        data={
            "Varianta": np.round(alpha, 3),
            "Varianta cumulata": np.round(np.cumsum(alpha), 3),
            "Procent varianta": np.round(alpha * 100 / sum(alpha), 3),
            "Procent cumulat": np.round(np.cumsum(alpha * 100 / sum(alpha)), 3)
        }, index=["Comp"+str(i+1) for i in range(len(alpha))]
    )