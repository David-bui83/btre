from django.contrib import admin
from .models import Listing

# Create model to customerize listing table on listing page
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'realtor') # diplaying columns
  list_display_links = ('id', 'title') # Create links 
  list_filter = ('realtor',) # filter by
  list_editable = ('is_published',) # editable
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') # create search 
  list_per_page = 25 # capping number to display per page


# Register your models here
admin.site.register(Listing, ListingAdmin)
