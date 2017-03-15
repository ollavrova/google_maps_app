from app.models import Coordinates
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase


class TestApp(TestCase):
    """
    test case for application
    """

    def setUp(self):
        user = User.objects.create(username='admin34534543512132',
                                   is_active=True,
                                   email='asd@goolf.com')
        user.set_password('555')
        user.save()
        self.auth = {"username": user.username, "password": '555'}
        self.coord = Coordinates.objects.create(
            address="Something address",
            lat="1234567890",
            lng="qwerty qwerty",
        )
        self.coord1 = Coordinates.objects.create(
            address="Some another address",
            lat="98765432109876",
            lng="qwert3423y qwerty34234",
        )

    def test_auth(self):
        """
        testing auth - if we have a page with login required
        """
        self.assertEqual(self.client.get(reverse('logout')).
                         status_code, 302)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Imports application')
        self.assertContains(response, 'Find coordinates:')
        # self.assertContains(response, 'Submit')
        self.assertNotContains(response, 'Saved results')

        self.client.post(reverse('login'), self.auth)
        response1 = self.client.get(reverse('home'))
        self.assertContains(response1, 'Logout')
        self.assertContains(response1, 'Saved results')
        self.assertContains(response1, 'ID')
        self.assertContains(response1, 'Created')
        self.assertContains(response1, self.coord.address)
        self.assertContains(response1, self.coord.lat)
        self.assertContains(response1, self.coord.lng)
        self.assertContains(response1, self.coord1.address)
        self.assertContains(response1, self.coord1.lng)
        self.assertContains(response1, self.coord1.lng)

    def test_api(self):
        """
        testing if pages with list of coordinates and details exists,
        if they have got response 'ok' and contains actual data
        """
        response = self.client.get(reverse('coord_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.coord.address)
        self.assertContains(response, self.coord.lat)
        self.assertContains(response, self.coord.lng)
        self.assertContains(response, self.coord1.address)
        self.assertContains(response, self.coord1.lat)
        self.assertContains(response, self.coord1.lng)

        response = self.client.get(reverse('coord_detail',
                                           kwargs={'pk': self.coord.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.coord.address)
        self.assertContains(response, self.coord.lat)
        self.assertContains(response, self.coord.lng)
        self.assertNotContains(response, self.coord1.address)
        self.assertNotContains(response, self.coord1.lat)
        self.assertNotContains(response, self.coord1.lng)

        response = self.client.get(reverse('coord_detail',
                                           kwargs={'pk': self.coord1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.coord1.address)
        self.assertContains(response, self.coord1.lat)
        self.assertContains(response, self.coord1.lng)
        self.assertNotContains(response, self.coord.address)
        self.assertNotContains(response, self.coord.lat)
        self.assertNotContains(response, self.coord.lng)
        self.assertNotContains(response, self.coord.created)
