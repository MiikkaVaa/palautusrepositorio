import unittest
from statistics_service import StatisticsService
from player import Player

class  PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieus", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_pelaaja_loydetaan_nimella(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
    
    def test_pelaajaa_ei_loydy_virheellisella_nimella(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)
    
    def test_tiimin_pelaajat_loydetaan(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in team_players))
    
    def test_top_pelaajat_palauttaa_oikean_maaran(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4)
    
    def test_top_pelaajien_järjestys_on_oikea(self):
        top_players = self.stats.top(2)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertTrue(top_players[0].points >= top_players[1].points)
        
        
