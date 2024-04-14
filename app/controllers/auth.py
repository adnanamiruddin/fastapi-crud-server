from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from app import app, SessionLocal
from app.models import DataDosen

auth_scheme = HTTPBearer()


class Settings(BaseModel):
    authjwt_secret_key: str = "SECRET_TOKEN"


@AuthJWT.load_config
def get_config():
    return Settings()


class LoginSchema(BaseModel):
    nip: str
    nama_lengkap: str


@app.post("/login")
def login(data: LoginSchema, authorize: AuthJWT = Depends()):
    db = SessionLocal()
    data_dosen = db.query(DataDosen).filter_by(nip=data.nip, nama_lengkap=data.nama_lengkap).first()

    if data_dosen is None:
        raise HTTPException(status_code=401, detail="Data dosen tidak ditemukan")

    access_token = authorize.create_access_token(subject=data.nip)
    return {"message": "Login berhasil", "access_token": access_token}


@app.get("/profile")
def profile(authorize: AuthJWT = Depends(), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    authorize.jwt_required()
    current_user = authorize.get_jwt_subject()

    return {"logged_in_as": current_user}
