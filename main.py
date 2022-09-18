<<<<<<< Updated upstream
=======
"""Main.py"""
from fastapi import  FastAPI

from pkg.application.core.environment import get_environment_variables
from pkg.domain.dao.models.base_model import init
from pkg.presentation.rest.user_routers import user_router


# Environment Configuration
env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
)

# Add Routers
app.include_router(user_router)

# Initialise Data Model Attributes
init()
>>>>>>> Stashed changes
