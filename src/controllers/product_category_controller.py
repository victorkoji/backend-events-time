from fastapi import APIRouter, Response, status
from services.product_category_service import ProductCategoryService
from schemas.product_category_schema import ProductCategoryCreateSchema, ProductCategorySchema
from fastapi.responses import JSONResponse
from typing import List

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
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.get('/{product_id}', response_model=ProductCategorySchema)
def get_product_category(product_id: int):
    try:
        product_categories = product_category_service.get(product_id)
        return product_categories.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/', response_model=ProductCategorySchema, status_code=status.HTTP_201_CREATED)
def add_product_category(product: ProductCategoryCreateSchema):
    try:
        product_category = product_category_service.add(product.dict())
        return product_category.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/', response_model=ProductCategorySchema)
def update_product_category(product: ProductCategorySchema):
    try:
        product_category = product_category_service.update(product.dict())
        return product_category.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_product_category(product_id):
    try:
        product_category_service.delete(product_id)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)
