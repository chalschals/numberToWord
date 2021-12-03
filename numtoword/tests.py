from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from num2words import num2words


class NumbersToWordTestCase(APITestCase):

    # FOR GET ENDPOINT
    def testGetRequestValidation1(self):
        url = reverse('num2word')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testGetRequestValidation2(self):
        url = reverse('num2word')
        response = self.client.get(url+'?number=tes', format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testGetRequest(self):
        url = reverse('num2word')
        testDigit = 12346
        response = self.client.get(
            url+'?number='+str(testDigit), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get(
            'num_to_english'), num2words(testDigit))

    # FOR POST ENDPOINT
    def testPostRequestValidation1(self):
        url = reverse('num2word')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testPostRequestValidation2(self):
        url = reverse('num2word')
        response = self.client.post(url, {'number': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testPostRequest(self):
        url = reverse('num2word')
        testDigit = 12346
        response = self.client.post(url, {'number': testDigit}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get(
            'num_to_english'), num2words(testDigit))
