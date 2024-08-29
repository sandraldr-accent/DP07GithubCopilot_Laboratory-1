from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo Pydantic para la entrada de texto
class TextInput(BaseModel):
    texto: str

# Punto de conexión para generar la suma de comprobación
@app.post("/generate")
def generate(input: TextInput):
    # Calcula la suma de comprobación del texto
    checksum = sum(ord(char) for char in input.texto)
    return {"checksum": checksum}

# Nota de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido, [Nombre del Participante]!"}

