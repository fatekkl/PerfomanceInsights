class Campaign:
    def __init__(self, date, name, platform, impressions, clicks, conversions, cost):
        self.date = date
        self.name = name
        self.platform = platform
        self.impressions = impressions
        self.clicks = clicks
        self.conversions = conversions
        self.cost = cost
        self.ctr = (clicks / impressions) * 100
        self.cpc = cost / clicks
        self.cpa = cost / conversions
        pass

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
            f"Cost: R$ {self.cost}\n"
            f"Click Through Rate (CTR): {self.ctr:.2f}%\n"
            f"Cost Per Click (CPC): R$ {self.cpc:.2f}\n"
            f"Cost Per Action (CPA): R$ {self.cpa:.2f}"
        )
