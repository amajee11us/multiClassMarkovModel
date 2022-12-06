import numpy as np
from prettytable import PrettyTable
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import math

from BTP import BTP

def getPerformanceScores(y_pred, y_true, type="classifier"):
    '''
    Implementation of RMSE and MAE scores for Collab Filtering
    and Accuracy, Precision, Recall, F1 score for Classifier
    '''
    if type == "classifier":
        conf_matrix = confusion_matrix(y_true, y_pred)

        precision = np.mean(np.diag(conf_matrix) / np.sum(conf_matrix, axis=0))

        recall = np.mean(np.diag(conf_matrix) / np.sum(conf_matrix, axis=1))

        F1 = (2 * precision * recall) / (precision + recall)

        accuracy = accuracy_score(y_true, y_pred)

        return accuracy, precision, recall, F1
    else:
        diff = y_true - y_pred

        abs_error = np.abs(diff)
        mean_abs_error = np.mean(abs_error) # this is MAE

        diff_square = np.square(diff)
        mean_sq_error = np.mean(diff_square)
        rmse = np.sqrt(mean_sq_error)

        return mean_abs_error, rmse

def printResults(result_row, table_columns=['Mean Absolute Error', 'RMSE']):
    # print the results in a table
    tab = PrettyTable(table_columns)
    tab.add_row(np.round(result_row,3))
    print(tab)

def computeErr(true_ll, pred_ll):
    return np.sum(true_ll)-np.sum(pred_ll)

def computeScore(err, max_err):
    return np.max((0, 100*(1.0-err/max_err)))

def computePerfScore(markov_net, X_test, y_test, y_pred, y_trivial, evid_var_ids, query_var_ids, order):
    '''
    Compute the Log probability and error and maxErr based on a trivial soln.
    '''
    def computeLogProb(X, y):
        out = np.zeros(X.shape[0])
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                markov_net.setEvidence(evid_var_ids[j], X[i][j])
            for j in range(y.shape[1]):
                markov_net.setEvidence(query_var_ids[j], y[i][j])
            btp = BTP(markov_net, order)
            out[i] = np.log10(btp.getPR())
        return out    
    lprob_true = computeLogProb(X_test, y_test)
    lprob_pred = computeLogProb(X_test, y_pred)
    lprob_trivial = computeLogProb(X_test, y_trivial)
    
    err = computeErr(lprob_true, lprob_pred)
    maxErr = computeErr(lprob_true, lprob_trivial)

    return err, maxErr
