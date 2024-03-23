import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def create_app(config="dev"):
    app = FastAPI(title="Lacanian Mind")
    app.add_middleware(
        CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'],
    )

    @app.post("/self")
    def self():
        return {"status": "healthy"}

    @app.post("/experience")
    def experience():
        return {"status": ""}

    return app

