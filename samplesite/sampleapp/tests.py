from django.test import TestCase
from django.contrib.auth.models import User


class HomeViewTest(TestCase):

    def test_page_is_loaded(self):
        # Issue a GET request
        response = self.client.get('/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_page_visit_count_displayed(self):
    	''' Visit count is calculated '''
    	# send 3 GET requests to home page
    	response = self.client.get('/')
    	response = self.client.get('/')
    	response = self.client.get('/')
    	# Check that the rendered context contains visit_count variable
        self.assertEqual((response.context['visit_count']), 4) # check if visit_count is 3
    
    def test_user_name_displayed(self):
    	user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword') # create a user
    	response = self.client.login(username="john",password="johnpassword") # do a login
    	response = self.client.get('/') # get the home page

    	self.assertEqual(("john" in response.content), True) # response contains the username
    	
