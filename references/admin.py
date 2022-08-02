from django.contrib import admin

from references.models import Room, Subject, Groups, Pair


@admin.register(Room)
class RoomModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Groups)
class GroupsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Pair)
class PairModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'index')
