from fastapi import APIRouter

from controllers import (
    product_controller, product_category_controller, user_controller, auth_controller, event_controller,
    stand_category_controller, stand_controller
)

private_api_router = APIRouter()
private_api_router.include_router(product_controller.router)
private_api_router.include_router(product_category_controller.router)
private_api_router.include_router(user_controller.router)
private_api_router.include_router(event_controller.router)
private_api_router.include_router(stand_category_controller.router)
private_api_router.include_router(stand_controller.router)

public_api_router = APIRouter()
public_api_router.include_router(auth_controller.router)
