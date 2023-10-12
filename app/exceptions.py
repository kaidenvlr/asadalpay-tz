from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=msg if msg else "Not found")


class BadRequestException(HTTPException):
    def __init__(self, msg: str = ""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg if msg else "Bad request")
