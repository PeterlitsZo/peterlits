from rest_framework.test import APIRequestFactory, APITestCase
from django.conf import settings


class UserTest(APITestCase):

    # Test 001: request about GET all user
    ###############################################################################################
    def test_get_user_1(self):
        response = self.client.get('/v1/user/')
        self.assertEuqal(response.data, {})

    # Test 002: use post to add a new user
    ###############################################################################################
    def test_add_user_1(self):
        response = self.client.get('/v1/user/')
        self.assertEuqal(response.data, {})

        self.client.post('/v1/user/', {
            'name': 'Peter',
            'password': 'TestTest',
            'email': 'p@e.ter',
            '__test__': 'true',             # if test, we can make it valid if its key equal with
                                            # the SECRET_KEY
            '__test_key__': settings.SECRET_KEY,
        })

        response = self.client.get('/v1/user/')
        self.assertEuqal(response.data, {'name': 'Peter', 'email': 'p@e.ter'})

    # Test 003: If to be vaild time past 15 days, and then: 1. click it to envaild - say no. 2. 
    # try to log up - remove and then create new obj.
    ###############################################################################################

