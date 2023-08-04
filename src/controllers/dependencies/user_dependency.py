from fastapi import Request


def get_user_token(request: Request):
    return request.state.user
