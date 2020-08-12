from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_list = [i.name for i in self.model._meta.fields]
        self.list_display = field_list
        self.list_display_links = field_list
