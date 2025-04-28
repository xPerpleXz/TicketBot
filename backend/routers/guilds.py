from fastapi import APIRouter
from backend.utils.database import db

router = APIRouter()

@router.get("/{guild_id}")
async def get_guild_config(guild_id: int):
    return await db.guilds.find_one({"guild_id": guild_id})

@router.post("/{guild_id}/update")
async def update_guild_config(guild_id: int, data: dict):
    await db.guilds.update_one({"guild_id": guild_id}, {"$set": data})
    return {"message": "Update erfolgreich"}
