import os
from symbol import parameters
import numpy as np
import math

# sklearn libraries
from sklearn.linear_model import LogisticRegression
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

# display results
from prettytable import PrettyTable

class TrivialClassifier:
    def __init__(self, model_name='lr'):
        self.model_name = model_name
        self.__init_model()

        self.model = MultiOutputClassifier(self.classifier)
        

    def __init_model(self):
        '''
        Generates a model based on two paramters:
        model_name : lr/ GPC/ randomForest 
        parameters : choice of parameters passed to the model from iterator
        returns:
        An object of the model with the parameters baked into it
        '''
        if self.model_name == 'lr':
            '''
            Parameters (in-order) : criterion, splitter, max_depth, max_features, ccp_alpha
            '''
            self.classifier = LogisticRegression(max_iter=1000
                                                    )
        elif self.model_name == 'gpc':
            kernel_func = 1.0 * RBF(4.0)
            self.classifier = GaussianProcessClassifier(kernel=kernel_func)
        elif self.model_name == "randomForest":
            self.classifier = RandomForestClassifier(n_estimators=10,  
                                                     max_depth=2,
                                                     verbose=1
                                                    )
        else:
            print("[Error] Your choice of classifier does not exist.")

    def trainval(self, X_train, Y_train, X_test, Y_test):
        '''
        Train and test a classifier with only a single parameter set
        Note: This is only called after the tuning process
        '''
        print("Running Model Type : {}".format(self.model_name))
        # Train the model on the complete val set
        self.model.fit(X_train, Y_train)
        print("Done.")
        # Return the evaluated results on the complete test set
        print("Running Model Prediction of Type : {}".format(self.model_name))
        return self.model.predict(X_test)
