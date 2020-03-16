"""Tests."""

from django.test import TestCase
from django.contrib.auth import get_user_model

from .. import MessagingError
from ..models import Messaging
from ..utils import notify, read


class GeneralTestCase(TestCase):
    """Tests for General functionality."""

    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        """Create Users."""
        cls.user1 = cls.User.objects.create_user(
            username='user1@gmail.com', password='password'
        )

        cls.user2 = cls.User.objects.create(
            username='user2@gmail.com', password='password'
        )

    def test_to_json_without_extra_data(self):
        """
        If the extra_data argument is ommitted,

        the default should be an empty dictionary
        """
        # Create notification
        notification = Messaging.objects.create(
            source=self.user2, source_display_name='User 2',
            recipient=self.user1, action='Notified',
            category='General notification', obj=1, url='http://example.com',
            short_description='Short Description', is_read=False,
        )

        self.assertEqual(
            notification.to_json(),
            {
                'source': self.user2.id, 'source_display_name': 'User 2',
                'recipient': self.user1.id, 'action': 'Notified',
                'category': 'General notification', 'obj': 1,
                'short_description': 'Short Description',
                'extra_data': {}, 'channels': '',
                'url': 'http://example.com', 'is_read': False
            }
        )

    def test_to_json_with_extra_data(self):
        """Test to_json method with extra data."""
        notification = Messaging.objects.create(
            source=self.user2, source_display_name='User 2',
            recipient=self.user1, action='Notified',
            category='General notification', obj=1, url='http://example.com',
            short_description='Short Description', is_read=False,
            extra_data={'hello': 'world'}
        )

        self.assertEqual(
            notification.to_json(),
            {
                'source': self.user2.id, 'source_display_name': 'User 2',
                'recipient': self.user1.id, 'action': 'Notified',
                'category': 'General notification', 'obj': 1,
                'short_description': 'Short Description', 'channels': '',
                'url': 'http://example.com', 'extra_data': {'hello': 'world'},
                'is_read': False,
            }
        )


class NotificationSignalTestCase(TestCase):
    """Tests for the notification signals."""

    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        """Create Users."""
        cls.user1 = cls.User.objects.create_user(
            username='user1@gmail.com', password='password'
        )

        cls.user2 = cls.User.objects.create(
            username='user2@gmail.com', password='password'
        )

    def test_user_cant_read_others_notifications(self):
        """A user should only be able to read THEIR notifications."""
        # Create Notification for User2
        notification = Messaging.objects.create(
            source=self.user1, source_display_name='User 1',
            recipient=self.user2, action='Notified',
            category='General notification', obj=1, url='http://example.com',
            is_read=False
        )

        # Try and Read the notification as User1
        self.assertRaises(
            MessagingError,
            read, notify_id=notification.id, recipient=self.user1
        )

    def test_user_can_read_notifications(self):
        """A user can read their notification"""
        # Create Notification for User1
        notification = Messaging.objects.create(
            source=self.user2, source_display_name='User 2',
            recipient=self.user1, action='Notified',
            category='General notification', obj=1, url='http://example.com',
            is_read=False
        )

        # Try and Read the notification as user1
        read(notify_id=notification.id, recipient=self.user1)

        notification.refresh_from_db()
        self.assertEqual(notification.is_read, True)

    def test_silent_notification(self):
        """Test Silent notifications."""
        notify(
            source=self.user2, source_display_name='User 2',
            recipient=self.user1, action='Notified',
            category='Silent notification', obj=1, url='http://example.com',
            short_description='Short Description', is_read=False, silent=True,
            channels=('console',)
        )

        notifications = Messaging.objects.all()

        self.assertEqual(tuple(notifications), tuple())


class JSONFieldTestCase(TestCase):
    """Test the Custom JSONField."""

    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        """Create Users."""
        cls.user1 = cls.User.objects.create_user(
            username='user1@gmail.com', password='password'
        )

        cls.user2 = cls.User.objects.create(
            username='user2@gmail.com', password='password'
        )

    def test_raise_exception(self):
        """
        Should raise an exception

        When we try to save objects that can be serialized by the json module.
        """
        kwargs = {
            'sender': self.__class__, 'source': self.user2,
            'source_display_name': 'User 2', 'recipient': self.user1,
            'action': 'Notified', 'category': 'General notification',
            'obj': 1, 'short_description': 'Short Description',
            'url': 'http://example.com', 'is_read': False,
            'extra_data': {'hello': lambda x: 'world'},
            'channels': ('console',)
        }

        self.assertRaises(TypeError, notify, **kwargs)

    def test_json_decode(self):
        """Should return a dictionary back."""
        notify(
            source=self.user2, source_display_name='User 2',
            recipient=self.user1, action='Notified',
            category='Notification with extra data', obj=1,
            url='http://example.com', short_description='Short Description',
            is_read=False, extra_data={'hello': 'world'},
            channels=('console',)
        )

        notification = Messaging.objects.last()

        self.assertEqual(
            notification.extra_data, {'hello': 'world'}
        )


class TestListField(TestCase):
    """Tests for the list field."""

    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        """Create Users."""
        cls.user1 = cls.User.objects.create_user(
            username='user1@gmail.com', password='password'
        )

        cls.user2 = cls.User.objects.create(
            username='user2@gmail.com', password='password'
        )

    def test_should_return_list(self):
        """Should return a list of channels back."""
        notify(
            source=self.user2, source_display_name='User 2',
            recipient=self.user1, action='Notified',
            category='Notification with extra data', obj=1,
            url='http://example.com', short_description='Short Description',
            is_read=False, extra_data={'hello': 'world'},
            channels=('console', 'console')
        )

        notification = Messaging.objects.last()

        self.assertEqual(
            notification.to_json()['channels'], ['console', 'console']
        )
