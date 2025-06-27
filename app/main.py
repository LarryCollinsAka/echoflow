from fastapi import FastAPI
from settings import settings
from routers import users, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

#Cors
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# You can uncomment these when ready
# app.include_router(meetings.router, prefix="/meetings", tags=["Meetings"])
# app.include_router(summaries.router, prefix="/summaries", tags=["Summaries"])
# app.include_router(protected.router, prefix="/protected", tags=["Protected"])

@app.get("/")
def read_root():
    return {"msg": f"Welcome to {settings.APP_NAME}!"}