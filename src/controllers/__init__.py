from fastapi import APIRouter

from controllers import (
    product_controller, product_category_controller, user_controller, auth_controller, event_controller,
    stand_category_controller, stand_controller
)

from controllers.mobile import (
    event_controller as mobile_event_controller
)

private_api_router = APIRouter()
private_api_router.include_router(product_controller.router)
private_api_router.include_router(product_category_controller.router)
private_api_router.include_router(user_controller.router)
private_api_router.include_router(event_controller.router)
private_api_router.include_router(stand_category_controller.router)
private_api_router.include_router(stand_controller.router)
private_api_router.include_router(auth_controller.router_private)

public_api_router = APIRouter()
public_api_router.include_router(auth_controller.router_public)


# Mobile
private_api_router.include_router(mobile_event_controller.router)
