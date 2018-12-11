from django.contrib import admin

# Register listings - bring in Listing model
from .models import Listing
# Show more columns in admin section for listings
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'agent')
  list_display_links = ('id', 'title')
  list_filter = ('agent',)
  # Unpublish ability
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'province', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)

