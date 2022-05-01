from datetime import date
from ninja import Schema


# Campaign
# in and out
class CampaignInput(Schema):
    # owner:str --> ForeignKey?????
    campaign_name:str 
    is_active:bool 
    created_at:date
    updated_at:date

class CampaignOutput(Schema):
    id:int
    # owner:str
    campaign_name:str 
    is_active:bool 
    created_at:date
    updated_at:date



# Ad Group
# in and out
class AdGroupInput(Schema):
    # campaign:str 
    ad_group_name:str 
    is_active:bool 
    created_at:date
    updated_at:date

class AdGroupOutput(Schema):
    id:int
    # campaign:str 
    ad_group_name:str 
    is_active:bool 
    created_at:date
    updated_at:date




# Ads
# in and out
class AdsInput(Schema):
    # ad_group:str 
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

class AdsOutput(Schema):
    id:int
    # ad_group:str 
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