from typing import List
from fastapi import APIRouter, status, HTTPException
from services.product_service import ProductService
from schemas.product_category_schema import MenuSchema
from exceptions.product_exception import ProductNotFound
from utils.logger import Logger

logger = Logger("ProductController")

product_service = ProductService()
router = APIRouter(
    prefix="/mobile/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.get('/menu', response_model=List[MenuSchema])
def get_menu(event_id: int):
    try:
        products = product_service.get_menu_by_event_id(event_id)
        return products

    except Exception as ex:
        raise handle_exception(ex)

def handle_exception(ex):
    message_error = str(ex)

    if isinstance(ex, ProductNotFound):
        status_code = status.HTTP_404_NOT_FOUND

    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return HTTPException(status_code=status_code, detail=message_error)
