from django.contrib import admin
from django import forms
from django.core.files.images import get_image_dimensions
from django.utils.safestring import mark_safe
# Register your models here.

from touchcore.rest.models import Employee
from touchcore.rest.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
    def clean_logo(self):
        """
        Ensure picture is at least 100 by 100
        """
        logo = self.cleaned_data.get("logo")
        if logo:
            w, h = get_image_dimensions(logo)
            if w < 100 or h < 100:
                raise forms.ValidationError("Image should be at least 100x100 pixels")
        return logo

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_per_page = 10
    readonly_fields = ('logo_tag',)

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_per_page = 10

admin.site.register(Company, CompanyAdmin, )
admin.site.register(Employee, EmployeeAdmin, )
