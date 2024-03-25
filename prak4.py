class Praktikan:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai 
        
    def Data(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nNilai: {self.nilai}\n"
    
praktikan1 = Praktikan("Syahrul", "064002300031", 95)
teman1 = Praktikan("ijul", "064002300025", 89)
teman2 = Praktikan("ocan", "064002300041", 93)
teman3 = Praktikan("rangga", "064002300025", 90)

print("---Data Pribadi---")
print(praktikan1.Data())
print("---Data Teman ke 1---")
print(teman1.Data())
print("---Data Teman ke 2---")
print(teman2.Data())
print("---Data Teman ke 3---")
print(teman3.Data())
