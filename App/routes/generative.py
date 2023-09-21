from App.controllers.transfroms_generetive import transformss
from fastapi import APIRouter

generator_router = APIRouter()

generator = transformss()

from fastapi import Body
@generator_router.get('/generete')
def index():
    return {'teste': 'funcionando' }

@generator_router.post('/generete')
def predict_price(data:dict):
    question = str(data['question'])
    awswers = generator(data['question'])
    return {
            "message": awswers[0]['generated_text'][(len(question))+1:]
            }