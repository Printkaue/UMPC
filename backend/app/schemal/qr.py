from pydantic import BaseModel, HttpUrl


class QRGenerateRequest(BaseModel):
    url: HttpUrl