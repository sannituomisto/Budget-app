import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti=Maksukortti(1000)

    def test_kassan_rahat_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')

    def test_edulliset_oikein(self):
        self.assertEqual(str(self.kassapaate.edulliset), '0')

    def test_maukkaat_oikein(self):
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kateisosto_edulliset_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100240')
        self.assertEqual(str(self.kassapaate.edulliset), '1')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kateisosto_edulliset_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kateisosto_maukkaat_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100400')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '1')

    def test_kateisosto_maukkaat_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    
    def test_korttiosto_edulliset_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '1')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_korttiosto_edulliset_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100))
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_korttiosto_maukkaat_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '1')

    def test_korttiosto_maukkaat_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(300))
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kortin_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100100')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')

    def test_kortin_lataaminen_ei_onnistu_jos_neg(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')