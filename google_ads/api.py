from typing import List

from ninja import NinjaAPI
from google_ads.schemas import (CampaignInput, CampaignOutput, AdGroupInput, AdGroupOutput,
                                AdsInput, AdsOutput)
from google_ads.models import Campaign, AdGroup, Ads

from django.shortcuts import get_object_or_404


api = NinjaAPI()



# CRUD Campaign

# Create Campaign
@api.post('campaign/')
def create_campaign(request, payload:CampaignInput):
    campaign = Campaign.objects.create(**payload.dict())
    return {"id":campaign.id}


# GET Campaign List
@api.get('campaigns/', response=List[CampaignOutput])
def get_campaign_list(request):
    qs = Campaign.objects.all()
    return qs


# GET Campaign Detail
@api.get('campaign/{campaign_id}/', response=CampaignOutput)
def get_campaign_detail(request, campaign_id:int):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return campaign


# UPDATE Campaign
@api.put('campaign/{campaign_id}/')
def update_campaign(request, campaign_id:int, payload:CampaignInput):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    for attr, value in payload.dict().items():
        setattr(campaign, attr, value)                                      # IDK this function
    campaign.save()
    return {'success': True}

# DELETE Campaign
@api.delete('campaign/{campaign_id}/')
def delete_campaign(request, campaign_id:int):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    campaign.delete()
    return {'success': True}






# CRUD Ad Group

# GET Ad Group List
@api.get('ad-groups/', response=List[AdGroupOutput])
def get_adgroup_list(request):
    qs = AdGroup.objects.all()
    return qs


# GET Ad Group Detail
@api.get('ad-group/{adgroup_id}/', response=AdGroupOutput)
def get_adgroup_detail(request, adgroup_id:int):
    ad_group = get_object_or_404(AdGroup, id=adgroup_id)
    return ad_group

# CREATE Ad Group
@api.post('ad-group/')
def create_adgroup(request, payload:AdGroupInput):
    ad_group = AdGroup.objects.create(**payload.dict())
    return {'id':ad_group.id}


# UPDATE Ad Group
@api.put('ad-group/{adgroup_id}/')
def update_adgroup(request, ad_group_id:int, payload:AdGroupInput):
    ad_group = get_object_or_404(AdGroup, id=ad_group_id)
    for attr, value in payload.dict().items():
        setattr(ad_group, attr, value)
    ad_group.save()
    return {'success': True}

# DELETE Ad Group
@api.delete('ad-group/{adgroup_id}/')
def delete_adgroup(request, adgroup_id:int):
    ad_group = get_object_or_404(AdGroup, id=adgroup_id)
    ad_group.delete()
    return {'success': True}



# CRUD Ads

# GET Ads List
@api.get("ads/", response=List[AdsOutput])
def get_ads_list(request):
    qs = Ads.objects.all()
    return qs

# GET Ads Detail
@api.get("ads/{ad_id}/", response=AdsOutput)
def get_ad_detail(request, ad_id:int):
    ad = get_object_or_404(Ads, id=ad_id)
    return ad
    

# CREATE Ads
@api.post("ads/")
def create_ad(request, payload:AdsInput):
    ad = Ads.objects.create(**payload.dict())
    return {'id': ad.id}


# UPDATE Ads
@api.put("ads/{ad_id}/")
def update_ad(request, ad_id:int, payload:AdsInput):
    ad = get_object_or_404(Ads, id=ad_id)
    for attr, value in payload.dict().items():
        setattr(ad, attr, value)
    ad.save()
    return {"success": True}


# DELETE Ads
@api.delete("ads/{ad_id}/")
def delete_ad(request, ad_id:int):
    ad = get_object_or_404(Ads, id=ad_id)
    ad.delete()
    return {"success": True}