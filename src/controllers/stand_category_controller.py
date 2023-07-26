from fastapi import APIRouter, Response, status
from services.stand_category_service import StandCategoryService
from schemas.stand_category_schema import StandCategoryCreateSchema, StandCategorySchema
from fastapi.responses import JSONResponse
from typing import List

stand_category_service = StandCategoryService()
router = APIRouter(
    prefix="/stand-categories",
    tags=["stand-categories"],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[StandCategorySchema])
def get_all_items():
    try:
        stand_categories = stand_category_service.get()
        return stand_categories.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.get('/{stand_category_id}', response_model=StandCategorySchema)
def get_stand_categories(stand_category_id: int):
    try:
        stand_category = stand_category_service.get(stand_category_id)
        if (stand_category):
            return stand_category.serialize()
        else:
            return JSONResponse(content={'message': 'Stand category not found!'}, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/', response_model=StandCategorySchema, status_code=status.HTTP_201_CREATED)
def add_stand_categories(stand_category: StandCategoryCreateSchema):
    try:
        stand_category = stand_category_service.add(stand_category.dict())
        return stand_category.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/', response_model=StandCategorySchema)
def update_stand_categories(stand_category: StandCategorySchema):
    try:
        stand_category = stand_category_service.update(stand_category.dict())
        return stand_category.serialize()
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)


@router.delete('/{stand_category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_stand_categories(stand_category_id):
    try:
        stand_category_service.delete(stand_category_id)
    except Exception as ex:
        return JSONResponse(content={'message': ex.message}, status_code=status.HTTP_400_BAD_REQUEST)
