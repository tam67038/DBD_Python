from fastapi import FastAPI
from app.routers import book, profile_req_log, bdex_router, InquirySHL_router
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:5173", "http://127.0.0.1:5173"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router)
app.include_router(profile_req_log.router)
app.include_router(bdex_router.router)
app.include_router(InquirySHL_router.router)