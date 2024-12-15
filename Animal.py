class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info(self):
        return f"Nama: {self.name}, Makanan: {self.makanan}, Hidup: {self.hidup}, Berkembang Biak: {self.berkembang_biak}"

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, ciri_ciri):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.ciri_ciri = ciri_ciri

    def suara(self):
        return f"{self.name} mengeluarkan suara khas amphibi."

    def info(self):
        return super().info() + f", Habitat: {self.habitat}, Ciri-ciri: {self.ciri_ciri}"

amphibi1 = Amphibi("Kodok", "Serangga", "Darat & Air", "Bertelur", "Air dan darat", "Kulit licin")
amphibi2 = Amphibi("Katak", "Serangga", "Darat & Air", "Bertelur", "Air dan darat", "Kulit lembab")
amphibi3 = Amphibi("Salamander", "Serangga", "Darat & Air", "Bertelur", "Darat", "Tubuh memanjang")


class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bulu, suhu_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bulu = bulu
        self.suhu_tubuh = suhu_tubuh

    def berjalan(self):
        return f"{self.name} berjalan dengan kaki."

    def info(self):
        return super().info() + f", Bulu: {self.bulu}, Suhu Tubuh: {self.suhu_tubuh}"

mamalia1 = Mamalia("Kelinci", "Rumput", "Darat", "Melahirkan", "Bulu lembut", "Suhu tubuh konstan")
mamalia2 = Mamalia("Singa", "Daging", "Darat", "Melahirkan", "Bulu tebal", "Suhu tubuh konstan")
mamalia3 = Mamalia("Gajah", "Rumput", "Darat", "Melahirkan", "Bulu tipis", "Suhu tubuh konstan")


class Karnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, gigi_tajam, kekuatan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.gigi_tajam = gigi_tajam
        self.kekuatan = kekuatan

    def berburu(self):
        return f"{self.name} sedang berburu mangsa."

    def info(self):
        return super().info() + f", Gigi Tajam: {self.gigi_tajam}, Kekuatan: {self.kekuatan}"

karnivora1 = Karnivora("Singa", "Daging", "Darat", "Melahirkan", "Gigi taring", "Kekuatan besar")
karnivora2 = Karnivora("Harimau", "Daging", "Darat", "Melahirkan", "Gigi taring", "Kekuatan besar")
karnivora3 = Karnivora("Serigala", "Daging", "Darat", "Melahirkan", "Gigi taring", "Kekuatan besar")

print(amphibi1.info())
print(amphibi2.info())
print(amphibi3.info())
print(mamalia1.info())
print(mamalia2.info())
print(mamalia3.info())
print(karnivora1.info())
print(karnivora2.info())
print(karnivora3.info())