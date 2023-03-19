from django.contrib import admin

from components.models import StatusUser, StatusDocType, StatusWorkType, StatusCalculation, Components, \
    Components_StatusCalculation, Components_StatusWorkType, Components_StatusDocType


class Components_StatusCalculationInline(admin.StackedInline):
    model = Components_StatusCalculation
    extra = 1


class Components_StatusWorkTypeInline(admin.StackedInline):
    model = Components_StatusWorkType
    extra = 1


class Components_StatusDocTypeInline(admin.StackedInline):
    model = Components_StatusDocType
    extra = 1


class ComponentsAdmin(admin.ModelAdmin):
    model = Components
    inlines = [Components_StatusCalculationInline, Components_StatusWorkTypeInline, Components_StatusDocTypeInline]
    list_display = ["id", "name", "data_id"]


class StatusUserAdmin(admin.ModelAdmin):
    model = StatusUser
    list_display = ["id", "name", ]


class StatusDocTypeAdmin(admin.ModelAdmin):
    model = StatusDocType
    list_display = ["id", "name", ]


class StatusWorkTypeAdmin(admin.ModelAdmin):
    model = StatusWorkType
    list_display = ["id", "name", ]


class StatusCalculationAdmin(admin.ModelAdmin):
    model = StatusCalculation
    list_display = ["id", "name", ]


admin.site.register(Components, ComponentsAdmin)
admin.site.register(StatusUser, StatusUserAdmin)
admin.site.register(StatusDocType, StatusDocTypeAdmin)
admin.site.register(StatusWorkType, StatusWorkTypeAdmin)
admin.site.register(StatusCalculation, StatusCalculationAdmin)
