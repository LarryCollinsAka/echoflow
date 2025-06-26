from fastapi import FastAPI
from settings import settings
from routers import users, auth

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(users.router, prefix="/users", tags=["Users"])
#app.include_router(meetings.router, prefix="/meetings", tags=["Meetings"])
#app.include_router(summaries.router, prefix="/summaries", tags=["Summaries"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
#app.include_router(protected.router, prefix="/protected", tags=["Protected"])

@app.get("/")
def read_root():
    return {"msg": f"Welcome to {settings.APP_NAME}!"}