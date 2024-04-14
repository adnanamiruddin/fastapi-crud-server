from app import app, SessionLocal
from app.models import DataDokumen


@app.post("/data-dokumen")
async def create_datadokumen(nip: str, type_dokumen: str, nama_dokumen: str, nama_file: str):
    db = SessionLocal()
    if type_dokumen != "file" and type_dokumen != "url":
        return {"message": "Tipe dokumen harus file atau url"}
    new_datadokumen = DataDokumen(nip=nip, type_dokumen=type_dokumen, nama_dokumen=nama_dokumen, nama_file=nama_file)
    db.add(new_datadokumen)
    db.commit()
    db.refresh(new_datadokumen)
    return {"message": "Data Dokumen berhasil ditambahkan"}


@app.get("/data-dokumen")
async def get_all_datadokumen():
    db = SessionLocal()
    datadokumens = db.query(DataDokumen).all()
    return datadokumens


@app.get("/data-dokumen/{id}")
async def get_datadokumen_by_id(id: int):
    db = SessionLocal()
    datadokumen = db.query(DataDokumen).filter(DataDokumen.id == id).first()
    return datadokumen


@app.put("/data-dokumen/{id}")
async def update_datadokumen(id: int, nip: str, type_dokumen: str, nama_dokumen: str, nama_file: str):
    db = SessionLocal()
    if type_dokumen != "file" and type_dokumen != "url":
        return {"message": "Tipe dokumen harus file atau url"}
    datadokumen = db.query(DataDokumen).filter(DataDokumen.id == id).first()
    datadokumen.nip = nip
    datadokumen.type_dokumen = type_dokumen
    datadokumen.nama_dokumen = nama_dokumen
    datadokumen.nama_file = nama_file
    db.commit()
    return {"message": "Data Dokumen berhasil diperbarui"}


@app.delete("/data-dokumen/{id}")
async def delete_datadokumen(id: int):
    db = SessionLocal()
    datadokumen = db.query(DataDokumen).filter(DataDokumen.id == id).first()
    db.delete(datadokumen)
    db.commit()
    return {"message": "Data Dokumen berhasil dihapus"}
