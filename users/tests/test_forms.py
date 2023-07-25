from django.contrib.auth import get_user_model
from django.test import TestCase

from allauth.account.forms import SignupForm

from users.forms import UserProfileForm, MembershipForm

User = get_user_model()


class UsersFormsTestCase(TestCase):

    def test_signup_form(self):
        form = SignupForm({
            'username': 'username',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form = SignupForm({
            'username': 'username2',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'passwordmismatch'
        })
        self.assertFalse(form.is_valid())
        # Since django-allauth 0.27.0, the "You must type the same password
        # each time" form validation error that can be triggered during
        # signup is added to the 'password2' field instead of being added to
        # the non field errors.
        self.assertIn('password2', form.errors)
        self.assertEqual(
            form.errors['password2'],
            ['You must type the same password each time.']
        )

    def test_duplicate_username(self):
        User.objects.create_user('username2', 'test@example.com', 'testpass')

        form = SignupForm({
            'username': 'username2',
            'email': 'test2@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_duplicate_email(self):
        User.objects.create_user('test1', 'test@example.com', 'testpass')

        form = SignupForm({
            'username': 'username2',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_newline_in_username(self):
        # Note that since Django 1.9, forms.CharField().strip is True
        # and it strips all whitespace characters by default so there
        # is no need to do anything on our side.
        #
        # django-allauth's default regex doesn't match '\n' at the
        # end of a string so as a result of this, users can signup
        # with a user name like 'username\n'.
        #
        # This is a problem when a user can fill the form via curl
        # and Content-Type header set to
        # 'application/x-www-form-urlencoded'.
        #
        # See #1045 and test_newline_in_username in
        # users/tests/test_views.py for details.
        form = SignupForm({
            'username': 'username\n',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertTrue(form.is_valid())

    def test_non_ascii_username(self):
        form = SignupForm({
            'username': 'fööpython',
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['username'],
            [
                'Enter a valid username. This value may contain only '
                'English letters, numbers, and @/./+/-/_ characters.'
            ]
        )

    def test_user_membership(self):
        form = MembershipForm({
            'legal_name': 'Some Name',
            'preferred_name': 'Sommy',
            'email_address': 'sommy@example.com',
            'city': 'Lawrence',
            'region': 'Kansas',
            'country': 'USA',
            'postal_code': '66044',
            'psf_announcements': True,
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['psf_code_of_conduct'],
            ['Agreeing to the code of conduct is required.']
        )


class UserProfileFormTestCase(TestCase):

    def test_unique_email(self):
        User.objects.create_user('stanne', 'mikael@darktranquillity.com', 'testpass')
        User.objects.create_user('test42', 'test42@example.com', 'testpass')

        form = UserProfileForm({
            'username': 'stanne',
            'email': 'test42@example.com',
            'search_visibility': 0,
            'email_privacy': 0,
        }, instance=User.objects.get(username='stanne'))
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'email': ['Please use a unique email address.']}
        )

    def test_case_insensitive_unique_username(self):
        User.objects.create_user('stanne', 'mikael@darktranquillity.com', 'testpass')
        User.objects.create_user('test42', 'test42@example.com', 'testpass')

        form = UserProfileForm({
            'username': 'Test42',
            'email': 'mikael@darktranquillity.com',
            'search_visibility': 0,
            'email_privacy': 0,
        }, instance=User.objects.get(username='stanne'))
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'username': ['A user with that username already exists.']}
        )
