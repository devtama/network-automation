import sys

print(sys.version)
print(sys.executable)
print(" ")

class Ojek:
    def __init__(self, nama, transisi, daerah):
        self.nama = nama
        self.transisi = transisi
        self.daerah = daerah

    def cek_id(self):
        print(f"Nama : {self.nama} \nTransisi : {self.transisi} \nDaerah : {self.daerah}")

ojek1 = Ojek("udin", "manual", "tegalega")
ojek1.cek_id()