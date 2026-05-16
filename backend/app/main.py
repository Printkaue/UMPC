from fastapi import FastAPI
from app.routes import qr_generate

app = FastAPI(title="Um pouco de tudo", version="1.0.0")


app.include_router(
    qr_generate.router,
    prefix="/api/v1/qr",
    tags=["POST"]
)

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
