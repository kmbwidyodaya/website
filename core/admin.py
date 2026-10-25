from django.contrib import admin

from .models import News, Event, Media


class UserAuthorAdminMixin:
    def get_form(self, request, obj=None, **kwargs):
        form_class = super().get_form(request, obj, **kwargs)
        author_name = request.user.get_full_name().strip() or request.user.get_username()

        class AuthorLockedForm(form_class):
            def __init__(self, *args, **form_kwargs):
                super().__init__(*args, **form_kwargs)
                self.fields["author"].disabled = True
                if obj is None:
                    self.initial["author"] = author_name

        return AuthorLockedForm

    def save_model(self, request, obj, form, change):
        if obj._state.adding:
            obj.author = request.user.get_full_name().strip() or request.user.get_username()
        super().save_model(request, obj, form, change)


@admin.register(News)
class NewsAdmin(UserAuthorAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_open_for_public')
    list_filter = ('is_open_for_public', 'date')

@admin.register(Media)
class MediaAdmin(UserAuthorAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'description')