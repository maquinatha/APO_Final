from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

#CORS: habilitar peticiones desde clientes que no están en mi dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    all_credentials=True,
    allow_methods=["*"],
    
)



@app.get("/sumar")
def sumar_numeros(a:b):
    return a+b