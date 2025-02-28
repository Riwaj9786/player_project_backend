from django.contrib import admin
from chat.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
   list_display = ('sender', 'get_content', 'timestamp')
   list_display_links = list_display
   readonly_fields = ('sender', 'content', 'timestamp')

   def get_content(self, obj):
      content = f"{obj.content[:5]}..."
      return content
   get_content.short_description = "Message"