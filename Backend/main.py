from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

#CORS: habilitar peticiones desde clientes que no están en mi dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=    ["*"]
    )



@app.get("/sumar")
def sumar_numeros(a:float , b:float):
    return a+b

@app.get("/resta")
def sumar_numeros(a:float , b:float):
    return a-b



