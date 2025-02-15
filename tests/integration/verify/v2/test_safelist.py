# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SafelistTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.safelist.create(phone_number="phone_number")

        values = {'PhoneNumber': "phone_number", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/SafeList/Numbers',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "GNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "phone_number": "+18001234567",
                "url": "https://verify.twilio.com/v2/SafeList/Numbers/+18001234567"
            }
            '''
        ))

        actual = self.client.verify.v2.safelist.create(phone_number="phone_number")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.safelist("phone_number").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/SafeList/Numbers/phone_number',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "GNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "phone_number": "+18001234567",
                "url": "https://verify.twilio.com/v2/SafeList/Numbers/+18001234567"
            }
            '''
        ))

        actual = self.client.verify.v2.safelist("phone_number").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.safelist("phone_number").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://verify.twilio.com/v2/SafeList/Numbers/phone_number',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.verify.v2.safelist("phone_number").delete()

        self.assertTrue(actual)
