from django.contrib import admin

# Agents - bring in Listing model
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'hire_date')
  list_display_links = ('id', 'name')
  search_fields = ( 'name',)
  list_per_page = 25

admin.site.register(Agent, AgentAdmin)


