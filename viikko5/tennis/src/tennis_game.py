class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def point_label(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"
        raise ValueError(f"Invalid points: {points}")
    
    def tie_score_label(self, points):
        if points >= 3:
            return "Deuce"
        return f"{self.point_label(points)}-All"
    
    def endgame_score_label(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return "Advantage player1"
        elif score_diff == -1:
            return "Advantage player2"
        elif score_diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def normal_score_label(self):
        return f"{self.point_label(self.player1_score)}-{self.point_label(self.player2_score)}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.tie_score_label(self.player1_score)
        
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.endgame_score_label()
        
        else:
            return self.normal_score_label()
        

