from typing import List
from fastapi import APIRouter, Response, status, HTTPException
from services.product_category_service import ProductCategoryService
from schemas.product_category_schema import ProductCategoryCreateSchema, ProductCategorySchema

product_category_service = ProductCategoryService()
router = APIRouter(
    prefix="/product-categories",
    tags=["products-categories"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[ProductCategorySchema])
def get_all_items():
    try:
        product_categories = product_category_service.get()
        return product_categories.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.get('/{product_id}', response_model=ProductCategorySchema)
def get_product_category(product_id: int):
    try:
        product_categories = product_category_service.get(product_id)
        return product_categories.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.post('/', response_model=ProductCategorySchema, status_code=status.HTTP_201_CREATED)
def add_product_category(product: ProductCategoryCreateSchema):
    try:
        product_category = product_category_service.add(product.dict())
        return product_category.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.put('/', response_model=ProductCategorySchema)
def update_product_category(product: ProductCategorySchema):
    try:
        product_category = product_category_service.update(product.dict())
        return product_category.serialize()
    except Exception as ex:
        raise handle_exception(ex)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_product_category(product_id):
    try:
        product_category_service.delete(product_id)
    except Exception as ex:
        raise handle_exception(ex)

def handle_exception(ex):
    message_error = str(ex)
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return HTTPException(status_code=status_code, detail=message_error)
