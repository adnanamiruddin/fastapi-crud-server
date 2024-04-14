from app import app, SessionLocal
from app.models import DataProdi


@app.post("/data-prodi")
async def create_dataprodi(kode_prodi: str, nama_prodi: str):
    db = SessionLocal()
    new_dataprodi = DataProdi(kode_prodi=kode_prodi, nama_prodi=nama_prodi)
    db.add(new_dataprodi)
    db.commit()
    db.refresh(new_dataprodi)
    return {"message": "Data Prodi berhasil ditambahkan"}


@app.get("/data-prodi")
async def get_all_dataprodi():
    db = SessionLocal()
    dataprodis = db.query(DataProdi).all()
    return dataprodis


@app.get("/data-prodi/{prodi_id}")
async def get_dataprodi_by_id(prodi_id: int):
    db = SessionLocal()
    dataprodi = db.query(DataProdi).filter(DataProdi.id == prodi_id).first()
    return dataprodi


@app.put("/data-prodi/{prodi_id}")
async def update_dataprodi(prodi_id: int, kode_prodi: str, nama_prodi: str):
    db = SessionLocal()
    dataprodi = db.query(DataProdi).filter(DataProdi.id == prodi_id).first()
    dataprodi.kode_prodi = kode_prodi
    dataprodi.nama_prodi = nama_prodi
    db.commit()
    return {"message": "Data Prodi berhasil diperbarui"}


@app.delete("/data-prodi/{prodi_id}")
async def delete_dataprodi(prodi_id: int):
    db = SessionLocal()
    dataprodi = db.query(DataProdi).filter(DataProdi.id == prodi_id).first()
    db.delete(dataprodi)
    db.commit()
    return {"message": "Data Prodi berhasil dihapus"}
