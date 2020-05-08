from django.contrib import admin
from .models import Realtor


# Create model to customerize realtor table on realtor page
class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'hire_date') # displaying columns
  list_display_links = ('id', 'name') # Create links
  search_fields = ('name',) # Create search
  list_per_page = 25 # capping number to display per page


# Register your models here.
