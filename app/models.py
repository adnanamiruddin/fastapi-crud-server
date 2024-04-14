from app import Base
from sqlalchemy import Column, Integer, String, Enum


class DataProdi(Base):
    __tablename__ = "data_prodi"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    kode_prodi = Column(String(5))
    nama_prodi = Column(String(100))


class DataDosen(Base):
    __tablename__ = "data_dosen"

    nip = Column(String(30), primary_key=True, index=True, unique=True)
    nama_lengkap = Column(String(100))
    prodi_id = Column(Integer)


class DataDokumen(Base):
    __tablename__ = "data_dokumen"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nip = Column(String(30))
    type_dokumen = Column(Enum("file", "url"))
    nama_dokumen = Column(String(255))
    nama_file = Column(String(255))
