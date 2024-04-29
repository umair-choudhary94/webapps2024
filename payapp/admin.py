from django.contrib import admin
from .models import *


class RequestedMoneyAdmin(admin.ModelAdmin):
    list_display = ('From', 'to', 'currency', 'amount', 'status')
    list_filter = ('status',)
    search_fields = ('From__user__username', 'to__user__username')

class TransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ('Sender', 'Reciver', 'currency', 'amount', 'rate', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('Sender__user__username', 'Reciver__user__username')

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('to', 'user', 'amount', 'currency', 'notification_type', 'timestamp', 'is_read')
    list_filter = ('notification_type', 'is_read')
    search_fields = ('to__user__username', 'user__user__username')

admin.site.register(reqeusted_money, RequestedMoneyAdmin)
admin.site.register(Transaction_History, TransactionHistoryAdmin)
admin.site.register(Notifications, NotificationsAdmin)
