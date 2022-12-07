import numpy as np
import os

from .loadData import LoadData
from pgmpy.inference import VariableElimination

class BayesianInference:
    def __init__(self, model, qvar_ids, evar_ids):
        self.model = model
        self.engine = VariableElimination(self.model)
        self.evid_ids = evar_ids
        self.query_ids = qvar_ids
    
    def __infer(self, query_var, evidences):
        '''
        Given an assignment of the query and evidences
        perform inference on markov model.
        '''
        result = self.engine.query(
                            [query_var], 
                            evidence=evidences
                            )
        print(result[query_var])
        return result

    def evaluate(self, x_test, y_test):
        res = []
        for evid,query in zip(x_test,y_test):
            evid_json = {}
            for id, evar in enumerate(self.evid_ids):
                evid_json[evar] = evid[id] 
            for qvar in self.query_ids:
                # TODO : Perform argmax operation
                res.append(self.__infer(
                                    str(qvar), 
                                    evid_json))
