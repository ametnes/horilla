import pytest
from django.test import TestCase

from django.conf import settings

# Create your tests here.
from django.core import mail

@pytest.fixture
def tc():
    return TestCase()


def test_send_email():
    settings.configure()

