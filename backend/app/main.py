from fastapi import FastAPI
from app.routes import qr_generate, qr_read

app = FastAPI(title="Um pouco de tudo", version="1.0.0")


app.include_router(
    qr_generate.router,
    prefix="/api/v1/qr",
    tags=["POST"]
)

app.include_router(
    qr_read.router,
    prefix="/api/v1/qr",
    tags=["QR CODE"]
)

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
