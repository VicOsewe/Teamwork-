from fastapi import FastAPI


def app():
    app = FastAPI(title="TeamWork", version="1.0.0")
    return app
