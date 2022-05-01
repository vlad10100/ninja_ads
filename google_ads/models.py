from django.db import models
from django.contrib.auth.models import User



# Account
#   User


# Campaign
class Campaign(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    campaign_name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'

    def __str__(self):
        return self.campaign_name


# Ad Group
class AdGroup(models.Model): 
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    ad_group_name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'AdGroup'
        verbose_name_plural = 'AdGroups'

    def __str__(self):
        return self.ad_group_name


# Ad
class Ads(models.Model):
    ad_group = models.ForeignKey(AdGroup, on_delete=models.CASCADE)

    ad_name = models.CharField(max_length=150)
    headline_1 = models.CharField(max_length=100, unique=True)
    headline_2 = models.CharField(max_length=100, unique=True, null=True, blank=True)
    headline_3 = models.CharField(max_length=100, unique=True, null=True, blank=True)

    description1 = models.CharField(max_length=250, unique=True)
    description2 = models.CharField(max_length=250, unique=True, null=True, blank=True)

    website_link = models.URLField(max_length=250)

    is_active = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'


    def __str__(self):
        return self.ad_name




# Miscellaneous 
# mixins for created_at and updated_at
