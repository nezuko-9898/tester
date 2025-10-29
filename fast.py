from fastapi import FastAPI,HTTPException
import json

app = FastAPI()


def load_data():
    with open('employe.json') as emp:
        data = json.load(emp)

        return data





@app.get('/')
def welcome():
    return {'Message':'Welcome come to website'}


@app.get('/about')
def about():
    return {'Message' : 'Welcome to Employee Management system'}



@app.get('/show')
def emp():
  data= load_data()
  return data



@app.get('/employe/{employee_id}')
def emp(employee_id):
    data = load_data()

    if employee_id in data:
        return data[employee_id]
    
    raise HTTPException (status_code=404,detail='employee not found')