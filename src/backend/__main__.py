import uvicorn
from .settings import settings

uvicorn.run(
    'backend.server:app',
    host=settings.host,
    port=settings.port,
    reload=True
)
