from fastapi import APIRouter
from services.product_category_service import ProductCategoryService
from schemas.product_category_schema import ProductCategoryCreateSchema, ProductCategorySchema
from fastapi.responses import JSONResponse
from typing import List
from exceptions.custom_exception import DatabaseError

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
        return JSONResponse(content=product_categories.serialize(), status_code=200)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.get('/{product_id}', response_model=ProductCategorySchema)
def get_product(product_id: int):
    try:
        product_categories = product_category_service.get(product_id)
        return JSONResponse(content=product_categories.serialize(), status_code=200)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.post('/')
def add_product(product: ProductCategoryCreateSchema):
    try:
        product_category_service.add(product.dict())
        return JSONResponse(content={'message': 'Product added successfully'}, status_code=201)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.put('/')
def update_product(product: ProductCategorySchema):
    try:
        product_category_service.update(product.dict())
        return JSONResponse(content={'message': 'Product updated successfully'}, status_code=200)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.delete('/{product_id}')
def delete_product(product_id):
    try:
        product_category_service.delete(product_id)
        return JSONResponse(content={'message': 'Product deleted successfully'}, status_code=200)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)
