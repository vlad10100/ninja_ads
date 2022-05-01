from typing import List

from ninja import NinjaAPI
from google_ads.schemas import (CampaignInput, CampaignOutput, AdGroupInput, AdGroupOutput,
                                AdsInput, AdsOutput)
from google_ads.models import Campaign, AdGroup, Ads

api = NinjaAPI()



# CRUD Campaign
@api.get('campaigns/', response=List[CampaignOutput])
def get_all_campaigns(request):
    qs = Campaign.objects.all()
    return qs


# CRUD Ad Group



# CRUD Ads
@api.get("ads/", response=List[AdsOutput])
def get_all_ads(request):
    qs = Ads.objects.all()
    return qs