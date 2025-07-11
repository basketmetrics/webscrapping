

class Quarters:
    def __init__(self):
        self.home_quarters = []
        self.away_quarters = []

    def __del__(self):
        del self.away_quarters
        del self.home_quarters