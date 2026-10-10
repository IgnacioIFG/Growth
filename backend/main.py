from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

# This tells SQLAlchemy to read your models and create the tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Growth API")

@app.get("/")
def read_root():
    return {"message": "¡API de Growth funcionando!"}

# Ejemplo de ruta para ver si la DB está viva
@app.get("/routines/")
def get_routines(db: Session = Depends(get_db)):
    #Here will be the logic to query routines. For now, we return something static.
    return {"status": "ok", "routines": []}