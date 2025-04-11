import pandas as pd
from models import Campaign

campaign_path = "campaigns.csv"

campaigns_df = pd.read_csv(campaign_path)

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

print(campaigns[0].get()["name"])
