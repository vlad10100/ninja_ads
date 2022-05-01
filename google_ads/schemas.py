from datetime import date
from ninja import Schema
from pydantic import BaseModel

from google_ads.models import Campaign, AdGroup, Ads

# User 
# class UserSchema(Schema):
#     id:int
#     username:str


# Campaign
# in and out
class CampaignInput(Schema):
    # owner:UserSchema         # ForeignKey
    campaign_name:str 
    is_active:bool 


class CampaignOutput(Schema):
    id:int
    # owner:UserSchema         # ForeignKey
    campaign_name:str 
    is_active:bool 
    created_at:date
    updated_at:date


# Ad Group
# in and out
class AdGroupInput(Schema):
    campaign_id:int       # ForeignKey
    ad_group_name:str 
    is_active:bool 


class AdGroupOutput(Schema):
    id:int
    campaign:CampaignOutput = None         # ForeignKey
    ad_group_name:str 
    is_active:bool 
    created_at:date
    updated_at:date




# Ads
# in and out
class AdsInput(Schema):
    ad_group_id:int          # ForeignKey
    ad_name:str 
    headline_1:str 
    headline_2:str 
    headline_3:str 
    description1:str 
    description2:str 
    website_link:str 
    is_active:bool 


class AdsOutput(Schema):
    id:int
    ad_group:AdGroupOutput = None          # ForeignKey
    ad_name:str 
    headline_1:str 
    headline_2:str 
    headline_3:str 
    description1:str 
    description2:str 
    website_link:str 
    is_active:bool 
    created_at:date
    updated_at:date