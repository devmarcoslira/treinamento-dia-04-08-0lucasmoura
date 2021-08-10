import pickle
from fastapi import FastAPI

app = FastAPI()
@app.post('/model')

def titanic(Sex:int, Age:int, Lifeboat:int, Pclass:int):
    """ Predizer se uma pessoa vai sobreviver ou não ao acidente do Titanic.

    Args:
        Sex (int): [Sexo 0 é masculino sexo 1 é feminino]
        Age (int): [Idade em forma fracionaria]
        Lifeboat (int): [Numero do salva barco vidas que a pessoa pegou]
        Pclass (int): [Classe no navio representado por um inteiro, onde 1 é primeira classe e 3 é classe economica]

    Returns:
        [Object]: Json de resposta da aplicação
    """
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
        predict = titanic.predict([[Sex, Age, Lifeboat, Pclass]])
        predict = int(predict) # transforma numpy.ndarray em inteiro para a resposta da API
        return {'survived': predict, "status": 200, "message": "Predict realizado com sucesso!"}

@app.get('/model')
def get():
    return {'hello':'test'}
