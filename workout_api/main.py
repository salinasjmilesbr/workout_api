# Alterado para fins de desafio

from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
