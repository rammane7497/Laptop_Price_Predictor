from flask import Flask, request, render_template
import utils
import config
import json

project_data = json.load(open(config.PROJECT_PATH, 'r'))

app = Flask(__name__)

@app.route("/")
def index():
    Company = project_data['Company']
    TypeName = project_data['TypeName']
    Cpu = project_data['Cpu']
    Ram = project_data['Ram']
    Gpu = project_data['Gpu']
    OpSys = project_data['OpSys']
    ScreenResolution = project_data['ScreenResolution']
    IPS_Display = ["no", "yes"]
    Touchscreen = ["no", "yes"]
    SSD = project_data['SSD']
    HDD = project_data['HDD']
    return render_template('index.html', Company=Company, TypeName=TypeName, Cpu=Cpu, Ram=Ram, Gpu=Gpu, OpSys=OpSys, IPS_Display=IPS_Display, Touchscreen=Touchscreen, SSD=SSD, HDD=HDD, ScreenResolution=ScreenResolution)

@app.route("/predict", methods = ['POST'])
def predict():
    user_data = request.form

    Laptop_Price = utils.LaptopPricePrediction(user_data)

    prediction = Laptop_Price.get_prediction()

    return str(prediction)

if __name__ == "__main__":
    app.run("0.0.0.0", port=config.PORT_NUMBER)