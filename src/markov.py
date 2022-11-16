import os, itertools
import pandas as pd
import numpy as np




class FunctionModel:

    """
    Init function expects a list of numbers in the format stated in Function Scopes
    See: https://uaicompetition.github.io/uci-2022/file-formats/model-format/
    """
    def __init__(self, function_line):
        self.FunctionLine = function_line
        self.VariablesInFunction = function_line[0]
        self.VariableIndexes = function_line[1:]
        self.Truth_Table = []

    def add_table(self, Domain_Mapping, list_of_values):
        var_range_list = []
        # Iterate over the functions, variables 
        for var_index in self.VariableIndexes:
            # Grab the domain/cardinality of the variable var_index
            var_range = list(range(Domain_Mapping[var_index]))
            # Create all values of the variable var_index 
            # If cardinality = 3, then var_range = [0,1,2]
            var_range_list.append(var_range)
        
        # Create truth table by combining all combinations
        i = 0
        # Handle normal case
        if ( len(var_range_list) != 1):
            for truth_entry in itertools.product(*var_range_list):
                self.Truth_Table.append((truth_entry, list_of_values[i]))
                i += 1
        # Single param case so dont use product
        else:
            for truth_entry in var_range_list[0]:
                self.Truth_Table.append(([truth_entry], list_of_values[i]))
                i += 1
    
    def create_dataframe(self):
        columns = list(self.VariableIndexes)
        columns.append('f')
        data = []
        for entry in self.Truth_Table:
            data_entry = list(entry[0])
            data_entry.append(entry[1])
            data.append(data_entry)
        return pd.DataFrame(columns=columns, data=data)


        



class MarkovModel:

    """
    Create Markov model object that will
    take a .UAI file and import the data to
    Pandas for us.
    """
    def __init__(self, filename = None):
        if ( filename == None ):
            return
        self.N = 0
        self.M = 0
        self.Domain_Mapping = []
        self.Functions = []
        self.Markov_Models = []
        self.import_markov_model(filename)

    """
    See: https://uaicompetition.github.io/uci-2022/file-formats/model-format/
    for details in how UAI file format is.
    """
    def import_markov_model(self, filename):
        f = open(filename, 'r')
        # First line is model. Should be Markov
        graphtype = f.readline().rstrip()
        if ( graphtype != 'MARKOV' ):
            print('UAI model is NOT MARKOV: ' + graphtype)
        # Second line is # of variables in network
        self.N = int(f.readline())
        # Third line is cardinalities (# values each variable can have)
        third_line = [eval(x) for x in f.readline().split()]
        # Iterate through the variable domains
        for i in range(len(third_line)):
            self.Domain_Mapping.append(third_line[i])
        # Fourth line is the number of functions
        fourth_line = f.readline()
        # Handle the example vs actual Sample case
        while ( fourth_line == '\n' ):
            fourth_line = f.readline()
        self.M = int(fourth_line)
        # Next M-lines are the functions
        for func_idx in range(self.M):
            next_function = [eval(x) for x in f.readline().split()]
            self.Functions.append(FunctionModel(next_function))
        
        #Line between sections is blank
        f.readline()

        # Function Specification follows
        for func_idx in range(self.M):
            # First line is blank
            # Handle the example vs actual Sample case in if block
            first_line = f.readline()
            # Second line is # of values in truth table
            second_line = first_line.split()
            if ( first_line == '\n' ):
                second_line = f.readline().split()
            
            # Handle the example vs actual Sample case in if block
            list_of_values = []
            items_in_function = int(second_line[0])
            if ( len(second_line) != 1):
                
                # Third line (and on depending on total) is all values
                list_of_values = [float(x) for x in second_line[1:]]
            else:
                # Third line (and on depending on total) is all values
                list_of_values = [float(x) for x in f.readline().split()]
            
            while ( items_in_function != len(list_of_values)):
                next_list_of_values = [float(x) for x in f.readline().split()]
                list_of_values.extend(next_list_of_values)
            self.Functions[func_idx].add_table(self.Domain_Mapping, list_of_values)
            markov_model = self.Functions[func_idx].create_dataframe()
            self.Markov_Models.append(markov_model)

            

        


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    filename = '../examples/1.uai'
    print('\nMarkov model from ' + filename + '\n')
    x = MarkovModel(filename)
    print('LENGTH: ' + str(len(x.Markov_Models)) + '\n')
    filename = '../examples/2.uai'
    print('\nMarkov model from ' + filename + '\n')
    y = MarkovModel(filename)
    print('LENGTH: ' + str(len(y.Markov_Models)) + '\n')
    for i in range(1,5):
        filename = '../examples/MLC/Sample_' + str(i) + '_MLC_2022.uai'
        print('\nMarkov model from ' + filename + '\n')
        z = MarkovModel(filename)
        print('LENGTH: ' + str(len(z.Markov_Models)) + '\n')


