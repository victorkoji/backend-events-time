from fastapi import APIRouter, Response, status
from services.product_service import ProductService
from schemas.product_schema import ProductCreateSchema, ProductSchema
from fastapi.responses import JSONResponse
from typing import List
from exceptions.custom_exception import DatabaseError

product_service = ProductService()
router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[ProductSchema])
def get_all_items():
    try:
        products = product_service.get()
        return products.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.get('/{product_id}', response_model=ProductSchema)
def get_product(product_id: int):
    try:
        product = product_service.get(product_id)
        if (product):
            return product.serialize()
        else:
            return JSONResponse(content={'message': 'Product not found!'}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/', response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreateSchema):
    try:
        product = product_service.add(product.dict())
        return product.serialize()
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/', response_model=ProductSchema)
def update_product(product: ProductSchema):
    try:
        product = product_service.update(product.dict())
        return product.serialize()
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_product(product_id):
    try:
        product_service.delete(product_id)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)
