from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemal.qr import QRGenerateRequest
from app.services.qr_generator import generate_qr_code

router = APIRouter()

@router.post("/generate_qr")
def generate(data: QRGenerateRequest):
    buffer = generate_qr_code(str(data.url))

    return StreamingResponse(
        buffer,
        media_type="image/png"
    )