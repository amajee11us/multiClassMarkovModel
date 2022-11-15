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
        self.Variable_Name_Mapping = []
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
        self.add_variables(third_line)
        # Fourth line is the number of functions
        self.M = int(f.readline())
        # Next M-lines are the functions
        for func_idx in range(self.M):
            next_function = [eval(x) for x in f.readline().split()]
            self.Functions.append(FunctionModel(next_function))
        
        # Function Specification follows
        for func_idx in range(self.M):
            # First line is blank
            f.readline()
            # Second line is # of values in truth table
            items_in_function = int(f.readline())
            # Third line (and on depending on total) is all values
            list_of_values = [float(x) for x in f.readline().split()]
            while ( items_in_function != len(list_of_values)):
                next_list_of_values = [float(x) for x in f.readline().split()]
                list_of_values.extend(next_list_of_values)
            self.Functions[func_idx].add_table(self.Domain_Mapping, list_of_values)
            markov_model = self.Functions[func_idx].create_dataframe()
            print(markov_model)
            print('\n')
            self.Markov_Models.append(markov_model)


    """
    Expects a list of variable cardinality values. (List of integers)
    Ex: Third line of UAI file. Others can be added later
    """
    def add_variables(self, cardinality_list):
        # Iterate through the variable domains
        for i in range(len(cardinality_list)):
            self.Domain_Mapping.append(cardinality_list[i])
            # Index will be the end of the list - 1
            var_index = len(self.Domain_Mapping) - 1
            # Make var name based on index as follows:
            # 0 = A, 1 = B, ..., 25 = Z, 26 = AA, ...
            # Only goes up to ZZ which is 700 indixes so should be enough...
            var_name = ''
            a_plus_index = ord('A') + var_index
            # If block for handling indexes greater than A-Z (0-25)
            if ( a_plus_index > ord('Z') ):
                tmp_index = var_index
                delta = ord('Z') - ord('A') + 1
                second_char = (int) (tmp_index / delta) - 1
                var_name += chr(ord('A') + second_char)
                tmp_index = tmp_index - ((second_char+1) * delta)
                a_plus_index = ord('A') + tmp_index
            var_name += chr(a_plus_index)
            self.Variable_Name_Mapping.append(var_name)

    """
    Helper function to map a string variable name to a variable index
    """
    def name_to_index(self, var_name):
        return self.Variable_Name_Mapping.index(var_name)

    """
    Helper function to map an index of a variable to a variable name
    """
    def index_to_name(self, var_index):
        return self.Variable_Name_Mapping[var_index]
            




        


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    filename = '../examples/1.uai'
    print('\nMarkov model from ' + filename + '\n')
    x = MarkovModel(filename)
    filename = '../examples/2.uai'
    print('\nMarkov model from ' + filename + '\n')
    y = MarkovModel(filename)


