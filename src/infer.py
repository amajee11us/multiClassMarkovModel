import numpy as np
import os

from .loadData import LoadData
from pgmpy.inference import VariableElimination

class BayesianInference:
    def __init__(self, model, qvar_ids, evar_ids, infer_single=False):
        self.model = model
        self.engine = VariableElimination(self.model)
        self.evid_ids = evar_ids
        self.query_ids = qvar_ids
        # perform inference on single var
        self.infer_single =  infer_single
    
    def __infer(self, query_var, evidences):
        '''
        Given an assignment of the query and evidences
        perform inference on markov model.
        '''
        result = self.engine.query(
                            [query_var], 
                            evidence=evidences,
                            elimination_order='MinWeight',
                            joint=False
                            )
        if self.infer_single:
            print(result[query_var])
            return np.argmax(result[query_var].values)
        else:
            res_assignment = []
            for var in query_var:
                print(result[var])
                res_assignment.append(np.argmax(result[var].values))
            return res_assignment

    def evaluate(self, x_test, y_test):
        res = []
        for evid,query in zip(x_test,y_test):
            evid_json = {}
            for id, evar in enumerate(self.evid_ids):
                evid_json[evar] = evid[id]
            if self.infer_single: 
                for qvar in self.query_ids:
                    res.append(self.__infer(
                                        str(qvar), 
                                        evid_json))
            else:
                qvar = [str(x) for x in self.query_ids]
                res.append(self.__infer(qvar, evid_json))
        
        return res
