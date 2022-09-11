
from fastapi import FastAPI
from pkg.presentation.config import prepare_server

 
app = prepare_server()
