from datetime import datetime
from sim import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(mahasiswa_id):
    return Tmahasiswa.query.get(int(mahasiswa_id))

class Tmahasiswa(db.Model, UserMixin): #tambahkan
    id = db.Column(db.Integer, primary_key=True)
    npm = db.Column(db.String(15), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    kelas = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(30), nullable=False, default='default.jpg')
    pengaduans = db.relationship('Tpengaduan', backref='mahasiswa',lazy=True)
    artikels = db.relationship('Tartikel', backref='mahasiswa',lazy=True)
    surats= db.relationship('Tsurat', backref='mahasiswa',lazy=True)

    def __repr__(self) :
        return f"Tsurat('{self.npm}','{self.nama}','{self.email}','{self.password}','{self.kelas}','{self.alamat}','{self.foto}')"

class Tpengaduan(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    subjek = db.Column(db.String(100), nullable=False)
    kategori= db.Column(db.String(50), nullable=False)
    detail_pengaduan= db.Column(db.String(300), nullable=False)
    tgl_post= db.Column(db.DateTime(100), nullable=False, default= datetime.utcnow)
    mahasiswa_id= db.Column(db.Integer, db.ForeignKey('tmahasiswa.id'))

    def __repr__(self):
        return f"Tpengaduan('{self.subjek}','{self.kategori}','{self.detail_pengaduan}','{self.tgl_post}')"

class Tartikel(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    judul = db.Column(db.String(100), nullable=False)
    kategori= db.Column(db.String(50), nullable=False)
    detail_artikel= db.Column(db.String(300), nullable=False)
    tgl_post= db.Column(db.DateTime(100), nullable=False, default= datetime.utcnow)
    mahasiswa_id= db.Column(db.Integer, db.ForeignKey('tmahasiswa.id'))

    def __repr__(self):
        return f"Tartikel('{self.judul}','{self.kategori}','{self.detail_artikel}','{self.tgl_post}')"

class Tsurat(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    subjek = db.Column(db.String(100), nullable=False)
    kategori= db.Column(db.String(50), nullable=False)
    detail_surat= db.Column(db.String(300), nullable=False)
    tgl_post= db.Column(db.DateTime(100), nullable=False, default= datetime.utcnow)
    mahasiswa_id= db.Column(db.Integer, db.ForeignKey('tmahasiswa.id'))

    def __repr__(self):
        return f"Tsurat('{self.subjek}','{self.kategori}','{self.detail_surat}','{self.tgl_post}')"