from fastapi import UploadFile, APIRouter, File, HTTPException
from app.services.qr_reader import read_qrcode

router = APIRouter()

@router.post("/read_qrcode")
async def read(file: UploadFile = File(...)):
    contents = await file.read()
    result = read_qrcode(contents)

    if not result:
        return HTTPException(
            status_code=404,
            detail="Qrcode não encontrado amigo :("
        )
    
    return {
        "content": result
    }
