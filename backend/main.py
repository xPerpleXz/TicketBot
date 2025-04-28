from fastapi import FastAPI
from backend.routers import guilds
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TicketBot Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(guilds.router, prefix="/api/guilds", tags=["Guilds"])
