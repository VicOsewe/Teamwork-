from fastapi import FastAPI



def app():
    app = FastAPI(title="TeamWork", version="1.0.0")
    app.include_router(prefix="/api/v1")
    return app