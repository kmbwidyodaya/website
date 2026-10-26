from datetime import timedelta

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.utils import timezone

from .admin import MediaAdmin, NewsAdmin
from .models import Event, Media, News


class AdminAuthorTests(TestCase):
    def test_author_field_is_visible_locked_and_uses_current_admin_name(self):
        user = get_user_model().objects.create_user(
            username="editor",
            first_name="Ivan",
            last_name="Ibrahim",
        )
        request = RequestFactory().get("/admin/")
        request.user = user

        for model_admin, model in (
            (NewsAdmin(News, admin.site), News),
            (MediaAdmin(Media, admin.site), Media),
        ):
            with self.subTest(model=model.__name__):
                form_class = model_admin.get_form(request)
                form = form_class(instance=model())

                self.assertIn("author", form.fields)
                self.assertTrue(form.fields["author"].disabled)
                self.assertEqual(form["author"].value(), "Ivan Ibrahim")

    def test_news_and_media_author_are_taken_from_creating_admin(self):
        user = get_user_model().objects.create_user(
            username="editor",
            first_name="Ivan",
            last_name="Ibrahim",
        )
        request = RequestFactory().post("/admin/")
        request.user = user

        admin_models = (
            (NewsAdmin(News, admin.site), News(title="Test News")),
            (MediaAdmin(Media, admin.site), Media(title="Test Media")),
        )

        for model_admin, obj in admin_models:
            with self.subTest(model=obj.__class__.__name__):
                model_admin.save_model(request, obj, form=None, change=False)
                self.assertEqual(obj.author, "Ivan Ibrahim")

                obj.title = f"Updated {obj.title}"
                model_admin.save_model(request, obj, form=None, change=True)
                self.assertEqual(obj.author, "Ivan Ibrahim")

    def test_username_is_used_when_admin_has_no_full_name(self):
        user = get_user_model().objects.create_user(username="editor")
        request = RequestFactory().post("/admin/")
        request.user = user
        obj = NewsAdmin(News, admin.site)

        news = News(title="Test News")
        obj.save_model(request, news, form=None, change=False)

        self.assertEqual(news.author, "editor")


class EventDetailTests(TestCase):
    def test_view_details_shows_full_event_description(self):
        event = Event.objects.create(
            title="KMB Gathering",
            full_description="Full event description",
            date=timezone.localdate() + timedelta(days=3),
        )

        response = self.client.get(f"/events/{event.pk}/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Full event description")

    def test_past_event_registration_is_disabled(self):
        event = Event.objects.create(
            title="Past Gathering",
            full_description="Past event details",
            date=timezone.localdate() - timedelta(days=1),
            registration_link="https://example.com/register",
        )

        response = self.client.get(f"/events/{event.pk}/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<button type="button" class="btn btn-disabled" disabled>Registration Closed</button>', html=True)
        self.assertNotContains(response, 'href="https://example.com/register"')

    def test_events_page_lists_upcoming_events(self):
        upcoming_event = Event.objects.create(
            title="Upcoming Gathering",
            full_description="Gathering details",
            date=timezone.localdate() + timedelta(days=3),
            registration_link="https://example.com/upcoming",
        )
        response = self.client.get("/events/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, upcoming_event.title)
        self.assertContains(response, "Gathering details")
        self.assertContains(response, 'href="https://example.com/upcoming"')
        self.assertNotContains(response, "There are no Upcoming Events right now")
        self.assertContains(response, "There are no Past Events right now")

    def test_events_page_shows_empty_messages_when_no_events(self):
        response = self.client.get("/events/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no Upcoming Events right now")
        self.assertContains(response, "There are no Past Events right now")

    def test_events_page_lists_past_events_after_upcoming_events(self):
        upcoming_event = Event.objects.create(
            title="Upcoming Event",
            full_description="Upcoming details",
            date=timezone.localdate() + timedelta(days=3),
        )
        past_event = Event.objects.create(
            title="Past Event",
            full_description="Past details",
            date=timezone.localdate() - timedelta(days=3),
            registration_link="https://example.com/past",
        )

        response = self.client.get("/events/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_event.title)
        self.assertContains(response, "Past details")
        self.assertContains(response, '<button type="button" class="btn btn-disabled" disabled>Registration Closed</button>', html=True)
        self.assertLess(
            response.content.index(b"Upcoming Event"),
            response.content.index(b"Past Events"),
        )
        self.assertLess(
            response.content.index(b"Past Events"),
            response.content.index(b"Past Event</h3>"),
        )
