from fastapi import APIRouter
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
        return JSONResponse(content=products.serialize(), status_code=200)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.get('/{product_id}', response_model=ProductSchema)
def get_product(product_id: int):
    try:
        product = product_service.get(product_id)
        if (product):
            return JSONResponse(content=product.serialize(), status_code=200)
        else:
            return JSONResponse(content={'message': 'Product not found!'}, status_code=404)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.post('/')
def add_product(product: ProductCreateSchema):
    try:
        product_service.add(product.dict())
        return JSONResponse(content={'message': 'Product added successfully'}, status_code=201)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.put('/')
def update_product(product: ProductSchema):
    try:
        product_service.update(product.dict())
        return JSONResponse(content={'message': 'Product updated successfully'}, status_code=200)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)


@router.delete('/{product_id}')
def delete_product(product_id):
    try:
        product_service.delete(product_id)
        return JSONResponse(content={'message': 'Product deleted successfully'}, status_code=200)
    except DatabaseError as ex:
        return JSONResponse(content={'message': ex.message}, status_code=400)
