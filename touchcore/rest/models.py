from django.db import models

# Create your models here.

class Company(models.Model):
    """
    Schema for a company
    """
    name = models.CharField(blank=False, max_length=256)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(max_length=256)
    logo = models.ImageField(upload_to="images/", null=True, blank=True)

    def logo_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.logo.url))
    
    logo_tag.short_description = "Company Logo"

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Employee(models.Model):
    """
    Schema for an Employee
    """
    firstname = models.CharField(blank=False, null=False, max_length=256)
    lastname = models.CharField(blank=False, null=False, max_length=256)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phonenumber = models.IntegerField(blank=True, null=True)


