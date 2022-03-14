# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI
from fastapi import status
import sql_app.main as app_daa

app = FastAPI(title="Vest Challenge Test API", description="API for the VEST recruitment process", version="1.0.1")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
    
app.include_router(app)

