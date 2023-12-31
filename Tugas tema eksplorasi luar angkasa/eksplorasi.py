class LuarAngkasa:
    def __init__(self, nama, ukuran, jarak_ke_bumi, orbit):
        self._nama = nama
        self._ukuran = ukuran
        self._jarak_ke_bumi = jarak_ke_bumi
        self._orbit = orbit
    
    def waktu_jalan(self):
        return self.jarak_ke_destinasi / self.kecepatan

    def tampil(self):
        print(
            "- Nama kapal:",self._nama,
            "\n- Jarak kapal dengan bumi:", self._jarak_ke_bumi,"km",
            "\n- Kapal sedang mengorbit di sekitar :", self._orbit,
            "\n- ukuran kapal luar angkasa ini: ", self._ukuran,"M",
            "\n")

    def kesimpulan(self):
        print("Dari data diatas dapat di tarik kesimpulan bahwa :",
            "\n- Estimasi Kapal luar angkasa bergerak sebanyak",self.tampilwaktu(),"KM",
            "\n- Kapal akan",self.apaberhasil())
        

class KapalLuarAngkasa(LuarAngkasa):
    def __init__(self, nama, ukuran, jarak_ke_bumi, orbit, bahan_bakar,
                 kecepatan, lama_waktu_mendarat):
        super().__init__(nama, ukuran, jarak_ke_bumi, orbit)
        self.bahan_bakar = bahan_bakar
        self.kecepatan = kecepatan
        self.lama_waktu_mendarat = lama_waktu_mendarat

    def totalwaktutempuh(self):
        return self.waktu_jalan() + self.lama_waktu_mendarat

class Planet(LuarAngkasa):
    def __init__(self, nama, ukuran, jarak_ke_bumi, orbit, populasi, iklim , suhu):
        super().__init__(nama, ukuran, jarak_ke_bumi, orbit)
        self.__populasi = populasi
        self.__iklim = iklim
        self.__suhu = suhu
    
    def tampil(self):
        print(
            "- Nama Planet:",self._nama,
            "\n- Jarak planet dengan bumi:", self._jarak_ke_bumi,"km",
            "\n- planet sedang mengorbit di sekitar :", self._orbit,
            "\n- Diameter planet ini: ", self._ukuran,"KM",
            "\n- Populasi planet ini :",self.__populasi,"orang", 
            "\n- Iklim di planet ini ", self.__iklim,
            "\n- Planet ini memiliki suhu rata rata",self.__suhu,"celcius")

class Destinasi(KapalLuarAngkasa):
    def __init__(self, nama, ukuran, jarak_ke_bumi, orbit, bahan_bakar, kecepatan, 
                lama_waktu_mendarat, nama_destinasi, jarak_ke_destinasi, bahkar_digunakan):
        super().__init__(nama, ukuran, jarak_ke_bumi, orbit, 
                        bahan_bakar, kecepatan, lama_waktu_mendarat)
        self.nama_destinasi = nama_destinasi
        self.jarak_ke_destinasi = jarak_ke_destinasi
        self.bahkar_digunakan = bahkar_digunakan

    def apaberhasil(self):
        berhasil = self.bahan_bakar - self.bahkar_digunakan
        if berhasil > 0 :
            return("Berhasil sampai destinasi")
        else:
            return("gagal karena Kehabisan bahan bakar")
    
    def tampil(self):
        print(
            "- Nama kapal:",self._nama,
            "\n- Jarak kapal dengan bumi:", self._jarak_ke_bumi,"km",
            "\n- Kapal sedang mengorbit di sekitar :", self._orbit,
            "\n- ukuran kapal luar angkasa ini: ", self._ukuran,"M",
            "\n- Tangki bahan bakar kapal saat ini :",self.bahan_bakar,"kg", 
            "\n- Kecepatan rata rata kapal ", self.kecepatan,"km/h",
            "\n- Estimasi lamanya kapal untuk mendarat :",self.lama_waktu_mendarat,"jam",
            "\n- Tujuan kapal luar angkasa saat ini :",self.nama_destinasi,
            "\n- Jarak kapal saat ini ke",self.nama_destinasi,"adalah", self.jarak_ke_destinasi,"km",
            "\n- Estimasi penggunaan bahan bakar :",self.bahkar_digunakan,
            "\n")

    def tampilwaktu(self):
        return self.totalwaktutempuh()

    def kesimpulan(self):
        print("Dari data diatas dapat di tarik kesimpulan bahwa :",
            "\n- estimasi Kapal luar angkasa bergerak sebanyak",self.tampilwaktu(),"KM",
            "\n- kapal akan",self.apaberhasil())

    def input_sendiri():
        apakah = input("Apakah anda ingin memasukan sendiri data kapal ? (y/n) : ")
        while apakah == "y":
            if apakah == "y":
                    kapal3 = Destinasi(
                        input("masukan nama kapal :"),
                        input("masukan ukuran kapal :"),
                        input("masukan jarak kapal ke bumi :"),
                        input("masukan nama kapal mengorbit saat ini :"),
                        input("masukan tangki bahan bakar saat ini :"),
                        input("masukan kecepatan kapal :"),
                        input("masukan estimasi lama kapal mendarat :"),
                        input("masukan nama destinasi kapal :"),
                        input("masukan jarak kapal ke destinasi :"),
                        input("masukan estimasi penggunaan bahan bakar :"),
                        )
                    print("="*60)
                    kapal3.tampil()
                    mau_ulang = input("apakah mau memasukan data lagi ? (y/n) : ")
                    if mau_ulang == "y":
                        continue
                    else:
                        exit()
        else:
            exit()
            
#mrnjalankan program               
print("="*60)
kapal1 = Destinasi("BTX01", 100, "100 juta", "Mars", 10000000, 1000, 2,"jupiter",600000000000,886)
kapal1.tampil()
kapal1.kesimpulan()
print("="*60)
planet1 = Planet("Jupiter","588 juta","139,822","Matahari",0," Badai terus menerus",-145)
planet1.tampil()
print("="*60)
Destinasi.input_sendiri()
print("="*60)