#! /user/bin/env python3

"""
Data Manager class to load the data and clean
"""

#from future import
__all__ = [
    'DataManager'
]
__version__ = "0.1.0.0"
__author__ = "Vidyadhar Bendre<vidyadhar.bendre@gmail.com>"
__maintainers__ = [
    "Vidyadhar Bendre<vidyadhar.bendre@gmail.com>"
]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from  sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# import train-test split 
from sklearn.model_selection import train_test_split

# import various functions from statsmodels
import statsmodels
import statsmodels.api as sm

# set the plot size using 'rcParams'
# once the plot size is set using 'rcParams', it sets the size of all the forthcoming plots in the file
# pass width and height in inches to 'figure.figsize' 
plt.rcParams['figure.figsize'] = [15,8]

class DataManager():
    def __init__(self, file_path):
        self.file_path = file_path
        self.target = None
        self.numeric_data = None
        self.categorical_data = None
        self.dummy_var = None
        self.df_std_scaled_data = None
        self.df_min_max_scaled_data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        # Create an empty dataframe to store the scores for various regression algorithms
        self.regression_score_card = pd.DataFrame(columns=['Algorithm', 'Mean Absolute Error', 'Mean Squared Error', 'Root Mean Squared Error', 'R-squared'])
        
        # create an empty dataframe to store the scores for various algorithms
        self.classification_score_card = pd.DataFrame(columns=['Probability Cutoff', 'AUC Score', 'Precision Score', 'Recall Score','Accuracy Score', 'Kappa Score', 'f1-score'])
        
        # assign 'score_card' as global variable
        global score_card
         
    def load_data(self):
        self.data = pd.read_csv(self.file_path)
    
    def display_initial_summary(self):

        # Print the shape of the dataframe
        print(f'The shape of the dataframe is {self.data.shape[0]} rows and {self.data.shape[1]} columns')

        # Display information about the dataframe
        print('\nInfo about the dataframe:')
        print(self.data.info())
        
        # Display the first few rows of the dataframe
        print('\nFirst few rows of the dataframe:')
        print(self.data.head())
   
        # Display the last few rows of the dataframe
        print('\nFirst few rows of the dataframe:')
        print(self.data.tail())
   
    
    def display_datatype(self):
        # Display data types of columns
        print('\nData types of columns:')
        print(self.data.dtypes)
            
    # def change_datatype(self):
    #     self.data['Research'] = self.data['Research'].astype(object)
    #     self.data['University Rating'] = self.data['University Rating'].astype(object)

    def display_missing_data(self):
        # sort the variables on the basis of total null values in the variable
        # 'isnull().sum()' returns the number of missing values in each variable
        # 'ascending = False' sorts values in the descending order
        # the variable with highest number of missing values will appear first
        Total = self.data.isnull().sum().sort_values(ascending=False)          

        # calculate percentage of missing values
        # 'ascending = False' sorts values in the descending order
        # the variable with highest percentage of missing values will appear first
        Percent = (self.data.isnull().sum()*100/self.data.isnull().count()).sort_values(ascending=False)   

        # concat the 'Total' and 'Percent' columns using 'concat' function
        # pass a list of column names in parameter 'keys' 
        # 'axis = 1' concats along the columns
        missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
        print(f'miissing_data', missing_data)
        
    def display_skew(self):
        # Calculate and display skewness for numeric columns
        numeric_columns = self.data.select_dtypes(include=[np.number])
        print('\nSkewness of numeric columns:')
        print(numeric_columns.skew())
        
    # def remove_insignificant_columns(self):
    #     # drop the column 'Serial No.' using drop()
    #     # 'axis = 1' drops the specified column
    #     self.data = self.data.drop('Serial No.', axis = 1)
        
    def plot_histogram(self):
        self.data.drop('Chance of Admit', axis = 1).hist()
        plt.tight_layout()
        plt.show()
       
    def split_cat_num_target(self):
        self.target = self.data['Chance of Admit'].copy()
        #print(f'target column', self.target)
        self.numeric_data = self.data.drop('Chance of Admit', axis = 1).select_dtypes(include=[np.number])    
        #print(f'The numeric columns are', self.numeric_data.columns)
        self.categorical_data = self.data.drop('Chance of Admit', axis = 1).select_dtypes(include=[np.object_]) 
        #print(f'The categorical columns are ', self.categorical_data.columns)
    
    
    def plot_countplot_target(self):
        # plot the countplot of the variable 'Chance of Admit'
        sns.countplot(x = self.target)

        # use below code to print the values in the graph
        # 'x' and 'y' gives position of the text
        # 's' is the text 
        plt.text(x = -0.05, y = self.target.value_counts()[0] + 1, s = str(round((self.target.value_counts()[0])*100/len(self.target),2)) + '%')
        plt.text(x = 0.95, y = self.target.value_counts()[1] +1, s = str(round((self.target.value_counts()[1])*100/len(self.target),2)) + '%')

        # add plot and axes labels
        # set text size using 'fontsize'
        plt.title('Count Plot for Target Variable (Chance of Admit)', fontsize = 15)
        plt.xlabel('Target Variable', fontsize = 15)
        plt.ylabel('Count', fontsize = 15)

        # to show the plot
        plt.show()
        
    
    def remove_na_null_numeric_data(self):
        self.numeric_data = self.numeric_data.dropna()
    
    def dummy_encode_categorical(self):
        self.dummy_var = pd.get_dummies(data=self.categorical_data.astype(str), drop_first=True)
        #print(f'The dummy encoded categorical data', self.dummy_var.columns)
        
    def std_scale_numeric_data(self):
        # initilize the standard scalar
        std_scalar = StandardScaler()
        std_scaled_data = std_scalar.fit_transform(self.numeric_data)
        self.df_std_scaled_data = pd.DataFrame(std_scaled_data, columns=self.numeric_data.columns)
        #print(f'standard scaled data', self.df_std_scaled_data.head()) 
        
    def min_max_scale_numeric_data(self):
        # initilize the standard scalar
        min_max_scalar = MinMaxScaler()
        min_max_scaled_data = min_max_scalar.fit_transform(self.numeric_data)
        self.df_min_max_scaled_data = pd.DataFrame(min_max_scaled_data, columns=self.numeric_data.columns)
        #print(f'min max scaled data', self.df_min_max_scaled_data.head())
        
    def combine_std_categorical(self):
        X = pd.concat([self.df_std_scaled_data, self.dummy_var], axis=1)
        y = self.target
        return X, y

    def combine_min_max_categorical(self):
        X = pd.concat([self.df_min_max_scaled_data, self.dummy_var], axis=1)
        y = self.target
        return X, y


