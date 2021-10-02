import pandas as pd
import sys
import numpy as np
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict, KFold, cross_val_score
import mlflow
import mlflow.sklearn 

# command line arguments are always passed as strings, so we need to parse them into the appropriate datatype
def input_to_string_list(arg):
    return arg.strip('[]').split(',')

#parse data into dataframes
def read_data(pathlist):
    df_list = []
    for path in pathlist:
        df = pd.read_csv(path, sep=',', header=0)
        df_list.append(df)
    return df_list

def inner_join(df_list):
    df1, df2 = df_list
    
    #hack to perform fast inner join on multiple keys
    df1['tempIndex']=df1['PlotName']+df1['ExperTag']+df1['RepeatText']+df1['TreatText']
    df2['tempIndex']=df2['PlotName']+df2['ExperTag']+df2['RepeatText']+df2['TreatText']

    # create inner join
    df = pd.concat([df1.set_index("tempIndex"),df2.set_index("tempIndex")], axis=1).reset_index()
    df = df.loc[:,~df.columns.duplicated()] #remove duplicate columns
    return df

def train(df):
    with mlflow.start_run():
        #training
        tmp = [i for i in df.columns if i[-2:] == '45'] #train only on '45' values
        reg=linear_model.LinearRegression(fit_intercept=False)
        kfold = KFold(n_splits=20)
        ypred = cross_val_predict(reg, df[tmp], df['NHI'], cv=kfold)
        temp = (ypred - df['NHI'])/df['NHI']*100
        temp = abs(temp)
        print('Mean percentage error:\t'+str(round(np.mean(temp),3))+' %')
        
        # log parameters, metrics and model to mlflow tracking server
        mlflow.log_param("fit_intercept", False)
        mlflow.log_metric("mean percentage error", round(np.mean(temp),3))
        mlflow.sklearn.log_model(reg, "model")
        
        return ypred
    return None

def present(ypred, df):
    temp = pd.DataFrame()
    temp['estim']=list(map(lambda x: abs(round(x, 1)),ypred))
    temp['nhi']=df['NHI']
    temp['error(%)']=list(map(lambda x: abs(round(x, 1)),(ypred-df['NHI'])/df['NHI']*100)) 
    
if __name__ == "__main__":
    # initialize mlflow tracking
    remote_server_uri = "http://127.0.0.1:5000"
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment("fertilizers")
    
    #dfs = read_data(['traits.csv', 'indices.csv'])
    dfs = read_data(input_to_string_list(sys.argv[1]))
    dataset = inner_join(dfs)
    predictions = train(dataset)
    present(predictions, dataset)
