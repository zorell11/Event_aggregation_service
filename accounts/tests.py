from django.test import TestCase
from .models import CustomUser
from .forms import UserSignUpForm


# Create your tests here.


class UsersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            username='custom_user@user.sk',
            email='custom_user@user.sk',
            password='pass',
            first_name='custom_user_first_name',
            last_name='custom_user_last_name',
            phone='123456',
            address='custom_user_test_address',
        )

    def test_get_billing_information(self):
        user = CustomUser.objects.get(email='custom_user@user.sk')
        self.assertEqual(user.get_billing_information(),
                         'custom_user_first_name custom_user_last_name\ncustom_user_test_address\n123456')


class UsersFromTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_user_form_is_valid(self):
        form = UserSignUpForm(data={
            'email': 'custom_user@user.sk',
            'first_name': 'custom_user_first_name',
            'last_name': 'custom_user_last_name',
            'password1': 'Test_pass123',
            'password2': 'Test_pass123',
            'phone': '123456',
            'address': 'custom_user_test_address',
        })

        self.assertTrue(form.is_valid())
