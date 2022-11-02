import pandas as pd
from functii import *

t_etnii = pd.read_csv("..\\data\\Ethnicity.csv", index_col=0)
nan_replace(t_etnii)

etnii = list(t_etnii)[1:] # preluam etniile intr-o lista

coduri_localitati = pd.read_csv("..\\data\\Coduri_Localitati.csv", index_col=0)
t_etnii = t_etnii[etnii].merge(coduri_localitati, left_index=True, right_index=True)
t_etnii.to_csv("..\\data\\t_etnii.csv")
t_etnii_judete = t_etnii[etnii+["County"]].groupby(by="County").agg(sum) # agg -> agregare
t_etnii_judete.to_csv("..\\data\\Etnii_judete.csv")

coduri_judete = pd.read_csv("..\\data\\Coduri_Judete.csv", index_col=0)
t_etnii2 = t_etnii_judete.merge(coduri_judete, left_index=True, right_index=True)
t_etnii_regiuni = t_etnii2[etnii+["Regiune"]].groupby(by="Regiune").agg(sum) # agg -> agregare
t_etnii_regiuni.to_csv("..\\data\\Etnii_regiuni.csv")

coduri_regiuni = pd.read_csv("..\\data\\Coduri_Regiuni.csv", index_col=0)
t_etnii3 = t_etnii_regiuni.merge(coduri_regiuni, left_index=True, right_index=True)
t_etnii_macroregiuni = t_etnii3[etnii+["MacroRegiune"]].groupby(by="MacroRegiune").agg(sum)
t_etnii_macroregiuni.to_csv("..\\data\\Etnii_macroregiuni.csv")

# Cerinta 2
t_disimilaritate = t_etnii[etnii+["County"]].groupby(by="County").apply(func=f_disimilaritate)
t_disimilaritate.to_csv("..\\data\\Disimilaritate.csv")

t_shannon = t_etnii[etnii+["County"]].groupby(by="County").apply(func=f_shannon)
t_shannon.to_csv("..\\data\\Shannon.csv")