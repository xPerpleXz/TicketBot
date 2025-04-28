import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.ticketbot

async def get_ticket_config(guild_id):
    return await db.guilds.find_one({"guild_id": guild_id})

async def save_ticket(channel_id, user_id):
    await db.tickets.insert_one({"channel_id": channel_id, "user_id": user_id})
