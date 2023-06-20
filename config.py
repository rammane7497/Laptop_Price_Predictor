import os

BASE_PATH = os.getcwd()

CSV_PATH = os.path.join(BASE_PATH, r"csv_files/cleaned_laptop_data.csv")

PROJECT_PATH = os.path.join(BASE_PATH, r"artifacts/project_data.json")

MODEL_PATH = os.path.join(BASE_PATH, r"artifacts/model_pipe.pkl")

PORT_NUMBER = 7777