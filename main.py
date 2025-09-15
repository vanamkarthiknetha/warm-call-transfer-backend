from fastapi import FastAPI, Query
import os
from livekit import api
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "success", "message": "Server is up and running in 8000 port"}


@app.get("/getToken")
def get_token(
    identity: str = Query(...), name: str = Query(...), room: str = Query(...)
):
    """
    Generate a LiveKit access token for a participant.
    - `identity`: Unique ID for the participant (e.g., "caller1", "agentA").
    - `name`: Display name in the LiveKit room.
    - `room`: Room name to join.
    """

    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

    if not LIVEKIT_API_KEY or not LIVEKIT_API_SECRET:
        return {"error": "Missing LiveKit API credentials"}

    # Build access token
    token = (
        api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
        .with_identity(identity)
        .with_name(name or identity)
        .with_grants(api.VideoGrants(room_join=True, room=room))
        .with_room_config(
            api.RoomConfiguration(
                agents=[
                    api.RoomAgentDispatch(agent_name="Warm-Transfer-Agent", metadata=f'{{"identity": "{identity}"}}')
                ],
            ),
        )
    )

    data = {
        "room": room,
        "identity": identity,
        "name": name,
        "token": token.to_jwt(),
    }

    return {
        "success": True,
        "data": data,
    }
