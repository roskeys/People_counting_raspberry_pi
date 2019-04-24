import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pickle
file = open("train_data.pickle","rb")
data = pickle.load((file))

def regression(data,seed):
    x = data["x"]
    y = data["y"]
    x_array = [[],[]]
    # test_y = []
    for i in x:
        # defined as the level difference between my current level and the level of the lift
        x_array[0].append(abs(i[1]-i[0]))
        # define the number of stops on the way of stopping
        x_array[1].append((len(i[2])))
        # test_y.append(abs(i[1]-i[0])*2 + len(i[2])*10 + 16)
    # reshape the x_array
    x_array = np.array(x_array).T
    y = np.array(y)
    # test_y = np.array(test_y)
    # error = sum(abs(y - test_y))
    X_train, X_test, Y_train, Y_test = train_test_split(x_array, y, test_size=30, random_state=seed)
    # use the linear model to fit
    regr = linear_model.LinearRegression().fit(X_train, Y_train)
    # predicting using test numbers 
    y_predict = regr.predict(X_test)
    # evaluate the model
    MSE = mean_squared_error(Y_test, y_predict)
    R2_score = r2_score(Y_test, y_predict)
    coefficients = regr.coef_
    intercept = regr.intercept_
    results = {'coefficients': coefficients, 'mean squared error': MSE, 'r2 score': R2_score, 'intercept': intercept}
    return regr,results
model,results = regression(data,1337)