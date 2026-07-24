from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from app.core.logger import logger


class QAPException(Exception):
    """
    Base exception for QAP.
    """

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(QAPException)
    async def qap_exception_handler(
        request: Request,
        exc: QAPException,
    ):
        logger.warning(
            f"QAPException | {request.method} {request.url.path} | {exc.message}"
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.message,
            },
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ):
        logger.warning(
            f"HTTPException | {request.method} {request.url.path} | {exc.detail}"
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.detail,
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            f"Unhandled Exception | {request.method} {request.url.path}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "Internal Server Error",
            },
        )