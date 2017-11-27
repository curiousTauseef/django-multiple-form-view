from django.test import TestCase


class ImportTest(TestCase):

    def test_import(self):
        from multiple_form_view import MultipleFormMixin, MultipleFormView  # noqa
