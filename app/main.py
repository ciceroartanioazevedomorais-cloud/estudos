from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.users import router as user_router
from app.core.exceptions import InvalidAgeException

app = FastAPI(title="Refactored User API")

@app.exception_handler(InvalidAgeException)
async def invalid_age_exception_handler(request: Request, exc: InvalidAgeException):
    return JSONResponse(
        status_code=400,
        content={"error": exc.message},
    )

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Refactored User API"}
