
# webapisoporteia

from fastapi import FastAPI

app = FastAPI(
    title="API Soporte IA",
    description="API para la pagina de Soporte IA",
    version="1.0.0"
)

##############################

#####
# Metodo Get
@app.get(
        "/metodoget",
        summary="Metodo Get",
        description="Metodo Get",
        tags=["Get"]
)
async def metodo_get(parametro:str):
    return parametro

##############################