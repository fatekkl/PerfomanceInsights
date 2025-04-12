import pandas as pd
from models import Campaign

campaign_path = "campaigns.csv"

campaigns_df = pd.read_csv(campaign_path)

# Dados que representam informações 'cruas', sem nenhuma métrica gerada

campaigns_data = campaigns_df.to_dict(orient="records")

campaigns = [
    Campaign(
        date=c["date"],
        name=c["name"],
        platform=c["platform"],
        impressions=int(c["impressions"]),
        clicks=int(c["clicks"]),
        conversions=int(c["conversions"]),
        cost=float(c["cost"]),
    )
    for c in campaigns_data
]


# Métricas de Click Through Rate (CTR), Cost Per Click (CPC) e Cost Per Action (CPA) criadas e convertidas em array

campaign_dict = [c.get() for c in campaigns]


handled_campaigns = pd.DataFrame(campaign_dict)


handled_campaigns.to_csv("handled_campaigns.csv", index=False)
