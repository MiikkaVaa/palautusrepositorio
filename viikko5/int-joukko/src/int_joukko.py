KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            kapasiteetti = KAPASITEETTI
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")  # heitin vaan jotain :D
        
        if kasvatuskoko is None:
            kasvatuskoko = OLETUSKASVATUS
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")  # heitin vaan jotain :D
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def etsi_indeksi(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if self.ljono[i] == luku:
                return i
        return -1
    
    def kasvata_taulukkoa(self):
        uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
        uusi_taulukko = self._luo_lista(uusi_koko)
        self.kopioi_lista(self.ljono, uusi_taulukko)
        self.ljono = uusi_taulukko

    def kuuluu(self, n):
        return self.etsi_indeksi(n) != -1

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        
        if self.alkioiden_lkm == len(self.ljono):
            self.kasvata_taulukkoa()
        
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1
        return True
    

    def poista(self, n):
        indeksi = self.etsi_indeksi(n)
        if indeksi == -1:
            return False
        
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        
        self.ljono[self.alkioiden_lkm - 1] = 0
        self.alkioiden_lkm -= 1
        return True

    def kopioi_lista(self, alkuperainen, kopio):
        for i in range(0, len(alkuperainen)):
            kopio[i] = alkuperainen[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(self.alkioiden_lkm):
            taulu[i] = self.ljono[i]

        return taulu

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        
        merkkijono = "{"
        for i in range(self.alkioiden_lkm):
            merkkijono += str(self.ljono[i])
            if i < self.alkioiden_lkm - 1:
                merkkijono += ", "
        merkkijono += "}"
        return merkkijono

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[luku])

        for luku in range(0, len(b_taulu)):
            tulos.lisaa(b_taulu[luku])
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()

        for luku in a.to_int_list():
            if b.kuuluu(luku):
                tulos.lisaa(luku)   

        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()

        for luku in a.to_int_list():
            tulos.lisaa(luku)

        for luku in b.to_int_list():
            tulos.poista(luku)
        return tulos
