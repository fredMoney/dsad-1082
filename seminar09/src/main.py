from functii import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB

tabel_invatare_testare = pd.read_csv("..//data//park.csv", index_col=0)
variabile = list(tabel_invatare_testare)
predictori = variabile[:-1]
tinta = variabile[-1]


# Splitare in set de antrenare si set de testare
x_train, x_test, y_train, y_test = train_test_split(
                                            tabel_invatare_testare[predictori],
                                            tabel_invatare_testare[tinta],
                                            test_size=0.4
                                            )


# Construire model liniar
model_lda = LinearDiscriminantAnalysis()
model_lda.fit(x_train, y_train)


# Preluare scoruri discriminante
clase = model_lda.classes_
q = len(clase) - 1 # q -> nr. functii discriminante
z = model_lda.transform(x_train)
for i in range(q):
    plot_distributie(z, y_train, i)

# show()

# Testare
predict_test_lda = model_lda.predict(x_test)
metrici_lda = calcul_metrici(y_test, predict_test_lda, clase)
metrici_lda[0].to_csv("..//data//results//MatC_LDA.csv")
metrici_lda[1].to_csv("..//data//results//Acuratete_LDA.csv")


# Aplicare model
x_apply = pd.read_csv("..//data//park_apply.csv", index_col=0)
predictie_lda = model_lda.predict(x_apply[predictori])
tabel_predictii = pd.DataFrame(
    data={
        "Predictie LDA:": predictie_lda
    }, index=x_apply.index
)


# Construire model bayesian
model_bayes = GaussianNB()
model_bayes.fit(x_train, y_train)

# Testare bayes
predict_test_b = model_bayes.predict(x_test)
metrici_b = calcul_metrici(y_test, predict_test_b, clase)
metrici_b[0].to_csv("..//data//results//MatC_B.csv")
metrici_b[1].to_csv("..//data//results//Acuratete_B.csv")

# Aplicare model
predictie_b = model_bayes.predict(x_apply[predictori])
tabel_predictii["Predictii Bayes"] = predictie_b
tabel_predictii.to_csv("..//data//results//Predictii.csv")