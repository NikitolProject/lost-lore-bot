from django.contrib import admin

from app import models

admin.site.register(models.BirthdaysEmployee)
admin.site.register(models.TemplatesForBirthday)
admin.site.register(models.AdsForEmployee)
admin.site.register(models.Channel)
