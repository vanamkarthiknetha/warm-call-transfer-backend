from dotenv import load_dotenv
import logging
from livekit import agents
from livekit.plugins import google
from livekit.agents import (
    Agent,
    AgentSession,
    AutoSubscribe,
    JobContext,
    RoomOutputOptions,
    WorkerOptions,
    cli,
)
from livekit.plugins import deepgram

load_dotenv()

logger = logging.getLogger("transcriber")


class Transcriber(Agent):
    def __init__(self):
        super().__init__(
            instructions="not-needed",
            stt=deepgram.STT(
                model="nova-3",
            ),
        )


async def entrypoint(ctx: JobContext):
    logger.info(f"starting transcriber (speech to text) example, room: {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    session = AgentSession()

    await session.start(
        agent=Transcriber(),
        room=ctx.room,
        room_output_options=RoomOutputOptions(
            transcription_enabled=False,
            audio_enabled=False,
        ),
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
