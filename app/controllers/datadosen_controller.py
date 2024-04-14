from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi_jwt_auth import AuthJWT
from app import app, SessionLocal
from app.models import DataDosen
from app.auth import auth_scheme


@app.post("/data-dosen")
async def create_datadosen(nip: str, nama_lengkap: str, prodi_id: int):
    db = SessionLocal()
    new_datadosen = DataDosen(nip=nip, nama_lengkap=nama_lengkap, prodi_id=prodi_id)
    db.add(new_datadosen)
    db.commit()
    db.refresh(new_datadosen)
    return {"message": "Data Dosen berhasil ditambahkan"}


@app.get("/data-dosen")
async def get_all_datadosen(authorize: AuthJWT = Depends(), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    authorize.jwt_required()
    db = SessionLocal()
    datadosens = db.query(DataDosen).all()
    return datadosens


@app.get("/data-dosen/{nip}")
async def get_datadosen_by_id(nip: str, authorize: AuthJWT = Depends(), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    authorize.jwt_required()
    db = SessionLocal()
    datadosen = db.query(DataDosen).filter(DataDosen.nip == nip).first()
    return datadosen


@app.put("/data-dosen/{nip}")
async def update_datadosen(nip: str, nama_lengkap: str, prodi_id: int):
    db = SessionLocal()
    datadosen = db.query(DataDosen).filter(DataDosen.nip == nip).first()
    datadosen.nama_lengkap = nama_lengkap
    datadosen.prodi_id = prodi_id
    db.commit()
    return {"message": "Data Dosen berhasil diperbarui"}


@app.delete("/data-dosen/{nip}")
async def delete_datadosen(nip: str):
    db = SessionLocal()
    datadosen = db.query(DataDosen).filter(DataDosen.nip == nip).first()
    db.delete(datadosen)
    db.commit()
    return {"message": "Data Dosen berhasil dihapus"}
