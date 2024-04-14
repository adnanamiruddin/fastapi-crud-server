from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configurations
SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost/db_repositori"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": "Token invalid atau tidak disediakan."}
    )


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 403 and exc.detail == "Not authenticated":
        return JSONResponse(
            status_code=403,
            content={
                "detail": "Akses ditolak. Anda tidak memiliki izin untuk mengakses rute ini tanpa token yang valid."}
        )
    # Else
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


from app import auth
from app.controllers import (
    dataprodi_controller,
    datadosen_controller,
    datadokumen_controller
)
