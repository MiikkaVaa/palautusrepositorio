import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorssa_on_yksi_tavara(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_ama_kuin_tuotteen_hinta(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("maito", 3)
        juusto = Tuote("juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("maito", 3)
        juusto = Tuote("juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_kaksi_kertaa_tuotteen_hinta(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisältää_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_yksi(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "maito")
        self.assertEqual(ostos.lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("maito", 3)
        juusto = Tuote("juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisältää_yhden_ostoksen(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lumumäärä_kaksi(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "maito")
        self.assertEqual(ostos.lukumaara(), 2)
    
    def test_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jää_koriin_ostos_jossa_tuotetta_yksi_kpl(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].lukumaara(), 1)
    
    def test_koriin_lisätty_tuote_poistetaan_ja_kori_on_tämän_jälkeen_tyhjä(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_tyhjenna_metodi_tyhjentaa_korin(self):
        maito = Tuote("maito", 3)
        juusto = Tuote("juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)