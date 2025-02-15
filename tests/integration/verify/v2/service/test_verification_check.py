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


class VerificationCheckTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verification_checks.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/VerificationCheck',
        ))

    def test_verification_checks_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sms",
                "status": "approved",
                "valid": true,
                "amount": null,
                "payee": null,
                "sna_attempts_error_codes": [],
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verification_checks.create()

        self.assertIsNotNone(actual)

    def test_email_verification_checks_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "recipient@foo.com",
                "channel": "email",
                "status": "approved",
                "valid": true,
                "amount": null,
                "payee": null,
                "sna_attempts_error_codes": [],
                "date_created": "2020-01-30T20:00:00Z",
                "date_updated": "2020-01-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verification_checks.create()

        self.assertIsNotNone(actual)

    def test_sna_verification_checks_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sna",
                "status": "approved",
                "valid": true,
                "amount": null,
                "payee": null,
                "sna_attempts_error_codes": [
                    {
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "code": 60001
                    }
                ],
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verification_checks.create()

        self.assertIsNotNone(actual)
