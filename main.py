import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./linear_regression_math/prix_maisons.csv")

def show_data(df):
    """
    1 - initialiser la figure
    2 - ajouter ce qu'on veut dessiner dans la figure
    3 - afficher le graphique
    """
    plt.figure(figsize=(8,6)) 
    plt.plot(df["surface"], df["prix"], "ro")
    plt.show()

# show_data(df)


def prepare_data(df):
    """
    this function will split the df into two sets of data : train and test
    """
    split_index = int(len(df) * 0.75)
    train_df, test_df = df.iloc[ : split_index], df.iloc[split_index : ]

    x_train = train_df[ ["surface"] ]
    y_train = train_df[ ["prix"] ]

    X_test = test_df[["surface"]]
    Y_test = test_df[["prix"]]

    return   x_train, y_train, X_test, Y_test

x_train, y_train, X_test, Y_test = prepare_data(df)

def regression(x_train, y_train):
    model = LinearRegression()
    model.fit (x_train, y_train)
    return model

def test_del (model, x_test, y_test):
    y_test_predicted = model.predict(x_test)

    plt.figure(figsize= (8 , 6))
    plt.plot (x_test, y_test, "bo")
    plt.plot (x_test, y_test_predicted, "ro")
    plt.show ()






 

