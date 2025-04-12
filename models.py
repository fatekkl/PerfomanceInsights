class Campaign:
    def __init__(self, date, name, platform, impressions, clicks, conversions, cost):
        self.date = date
        self.name = name
        self.platform = platform
        self.impressions = impressions
        self.clicks = clicks
        self.conversions = conversions
        self.cost = cost

        # Cálculos com tratamento de divisão por zero e arredondamento
        self.ctr = round((clicks / impressions) * 100, 2) if impressions > 0 else 0.0
        self.cpc = round(cost / clicks, 2) if clicks > 0 else 0.0
        self.cpa = round(cost / conversions, 2) if conversions > 0 else 0.0

    def get(self):
        return self.__dict__

    def __str__(self):
        return (
            f"Date: {self.date}\n"
            f"Name: {self.name}\n"
            f"Platform: {self.platform}\n"
            f"Impressions: {self.impressions}\n"
            f"Clicks: {self.clicks}\n"
            f"Conversions: {self.conversions}\n"
            f"Cost: R$ {self.cost:.2f}\n"
            f"Click Through Rate (CTR): {self.ctr:.2f}%\n"
            f"Cost Per Click (CPC): R$ {self.cpc:.2f}\n"
            f"Cost Per Action (CPA): R$ {self.cpa:.2f}"
        )
