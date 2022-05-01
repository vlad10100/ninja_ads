from django.contrib import admin

from google_ads.models import Campaign, AdGroup, Ads


admin.site.register(Campaign)
admin.site.register(AdGroup)
admin.site.register(Ads)