#file: app/backend/src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routers import file_router

app = FastAPI(
    title="processHub",
    version="1.0.1"
)

# Allow frontend to communicate with backend (adjust origin if needed)
origins = ["*"]
# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # <- This allows all origins
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],      # Allow all headers
)
app.include_router(file_router.api)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="localhost",  # Use localhost IP address
        port=8000,
        reload=True
    )