import config
import pickle
import pandas as pd
import numpy as np
import json
import sklearn

class LaptopPricePrediction():

    def __init__(self, data):
        self.data = data

    def load_data(self):
        self.model_pipe   = pickle.load(open(config.MODEL_PATH, 'rb'))
        self.project_data = json.load(open(config.PROJECT_PATH, 'r'))

    def get_prediction(self):
        Company      =  self.data['Company']
        TypeName     =  self.data['TypeName']
        Cpu          =  self.data['Cpu']
        Ram          =  int(eval(self.data['Ram']))
        Gpu          =  self.data['Gpu']
        OpSys        =  self.data['OpSys']
        Weight       =  eval(self.data['Weight'])
        IPS_Display  =  self.data['IPS_Display']
        Touchscreen  =  self.data['Touchscreen']
        Screen_Size  =  eval(self.data['Screen_Size'])
        ScreenResolution  = self.data['ScreenResolution']
        SSD          =  int(eval(self.data['SSD']))
        HDD          =  int(eval(self.data['HDD']))

        X_res = int(ScreenResolution.split("x")[0])
        Y_res = int(ScreenResolution.split("x")[1])
        PPI = np.round(((X_res**2 + Y_res**2)**0.5/Screen_Size),2)

        self.load_data()

        test_df = pd.DataFrame([[Company, TypeName, Cpu, Ram, Gpu, OpSys, Weight,
                        IPS_Display, Touchscreen, PPI, SSD, HDD]], columns=self.project_data['Column_Names'])

        predicted_price = int(np.round(np.exp(self.model_pipe.predict(test_df)[0])))

        return predicted_price
