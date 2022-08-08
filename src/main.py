from src.repositories.UserRepo import UserRepo
from src import constants
from dataclasses import asdict
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response, Request
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=constants.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root(response: Response, request: Request):
    response.set_cookie(key="fakesession",
                            value="fake-cookie-session-value")
    return asdict(UserRepo().get_user_by_id(1))
