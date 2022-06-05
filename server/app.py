from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.config.config_service import config_service
from src.db.db_service import db_service
from src.router.router_service import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
async def startup():
  await db_service.connect()

@app.on_event("shutdown")
async def shutdown():
  await db_service.disconnect()

def main():
  uvicorn.run('app:app', port=config_service.APP_PORT, host=config_service.APP_HOST, workers=2)

if __name__ == '__main__':
  main()
