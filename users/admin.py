from django.contrib import admin
from django.utils.html import format_html
import json

from .models import user, Token, DataShare, ShareNotification

class usersAdmin(admin.ModelAdmin):
    list_display=('email', 'password', 'fullName', 'fathersName', 'mothersName', 'gender', 'dateofbirth', 'category', 'disability', 'nationality', 'domicileState', 'maritalStatus', 'religion', 'permanentAddress', 'correspondenceAddress', 'phone_number', 'alt_phone_number', 'document_urls', 'document_texts')
    search_fields=('email', 'password', 'fullName', 'fathersName', 'mothersName', 'gender', 'dateofbirth', 'category', 'disability', 'nationality', 'domicileState', 'maritalStatus', 'religion', 'permanentAddress', 'correspondenceAddress', 'phone_number', 'alt_phone_number', 'document_urls', 'document_texts')
    list_filter=('email', 'password', 'fullName', 'fathersName', 'mothersName', 'gender', 'dateofbirth', 'category', 'disability', 'nationality', 'domicileState', 'maritalStatus', 'religion', 'permanentAddress', 'correspondenceAddress', 'phone_number', 'alt_phone_number', 'document_urls', 'document_texts')
    list_per_page=10

class DataShareAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'receiver_email', 'status', 'is_active', 'shared_at', 'responded_at', 'has_shared_data', 'selected_documents_count')
    list_filter = ('status', 'is_active', 'shared_at', 'responded_at')
    search_fields = ('sender_email', 'receiver_email')
    readonly_fields = ('shared_at', 'shared_data_preview', 'selected_documents_display')
    list_per_page = 20
    
    def has_shared_data(self, obj):
        return bool(obj.shared_data)
    has_shared_data.boolean = True
    has_shared_data.short_description = 'Has Data'
    
    def selected_documents_count(self, obj):
        if obj.selected_documents:
            return len(obj.selected_documents)
        return 0
    selected_documents_count.short_description = 'Docs Count'
    
    def selected_documents_display(self, obj):
        if obj.selected_documents:
            # Format the selected documents list nicely
            docs_list = "<br>".join([f"• {doc}" for doc in obj.selected_documents])
            return format_html('<div style="line-height: 1.5;">{}</div>', docs_list)
        return "No documents selected"
    selected_documents_display.short_description = 'Selected Documents'
    
    def shared_data_preview(self, obj):
        if obj.shared_data:
            # Format JSON for better readability
            formatted_json = json.dumps(obj.shared_data, indent=2)
            return format_html('<pre style="max-height: 400px; overflow-y: auto;">{}</pre>', formatted_json)
        return "No shared data"
    shared_data_preview.short_description = 'Shared Data (Preview)'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('sender_email', 'receiver_email', 'status', 'is_active')
        }),
        ('Selected Documents', {
            'fields': ('selected_documents_display',),
        }),
        ('Timestamps', {
            'fields': ('shared_at', 'responded_at', 'stopped_at')
        }),
        ('Shared Data', {
            'fields': ('shared_data_preview',),
            'classes': ('collapse',),
        }),
    )

class ShareNotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient_email', 'notification_type', 'is_read', 'created_at', 'data_share_info')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('recipient_email', 'message')
    readonly_fields = ('created_at',)
    list_per_page = 20
    
    def data_share_info(self, obj):
        return f"{obj.data_share.sender_email} -> {obj.data_share.receiver_email}"
    data_share_info.short_description = 'Data Share'
    
    fieldsets = (
        ('Notification Details', {
            'fields': ('data_share', 'recipient_email', 'notification_type', 'is_read')
        }),
        ('Content', {
            'fields': ('message',)
        }),
        ('Timestamp', {
            'fields': ('created_at',)
        }),
    )

admin.site.register(user, usersAdmin)
admin.site.register(Token)
admin.site.register(DataShare, DataShareAdmin)
admin.site.register(ShareNotification, ShareNotificationAdmin)


