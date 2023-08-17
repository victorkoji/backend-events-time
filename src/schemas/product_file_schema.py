from pydantic import BaseModel

class ProductFileSchema(BaseModel):
    id: int
    filename: str
    media_type: str
    filepath: str
