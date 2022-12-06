from src.loadData import LoadData
from src.classifier import TrivialClassifier
from MN import MN
from BTP import BTP

import os
from src.utils import *
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Assignment 4 : Markov Model for Query Assignment calculation.')

    # General parser
    parser.add_argument('--model_name',
                        default='Sample_1_MLC_2022',
                        type=str,
                        help='Name of the model file for which experiment is triggered.')
    parser.add_argument('--clf_name',
                        default='dtree',
                        type=str,
                        help='Name of the classifier used in thhe experiment. Example : dtree, bagging etc.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()

    # Step 1: Load the dataset file based on the argument passed
    print("[Data] Loading data {} ...".format(args.model_name))
    dataloader = LoadData(os.path.join("data/MLC", args.model_name + ".data"))

    X_train, Y_train, X_test, Y_test = dataloader.get_data_splits()

    # Step 2: Load the model file
    model_filename = os.path.join("data/MLC", args.model_name + ".uai")

    # Step 3: CLassifier 
    model = TrivialClassifier(model_name=args.clf_name)
    #params = pickBestParams(args.clf_name)
    y_pred = model.trainval(X_train, Y_train, X_test,Y_test)

    # Step 4: Trivial Classifier
    model_trivial = TrivialClassifier(model_name="randomForest")
    #params_trivial = pickBestParams("randomForest")
    y_pred_trivial = model_trivial.trainval(X_train, Y_train, X_test,Y_test)

    # Step 4: Initialize the Markov Network
    mn = MN()
    mn.read(model_filename)

    btp = BTP(mn)
    btp.getOrder(2) # min-fill ordering. Use 1 for min-degree
    order = np.asarray(btp.order)

    # Step 5: Perform performance scoring
    error, maxError = computePerfScore(mn, 
                            X_test, Y_test, 
                            y_pred, y_pred_trivial, 
                            dataloader.indexObservedVariables,
                            dataloader.indexQueryVariables,
                            order)
    
    # Step 6: Display Results
    printResults([error, maxError], ["Error", "Max-Error"])