from pkg.presentation.rest.rest import app
from pkg.infrastructure.database.postgres.database import TeamWorkDB


def prepare_server():
    a = app()
    db = TeamWorkDB()
    return app
