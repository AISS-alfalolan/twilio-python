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


class ContentTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.content.v1.contents("HXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://content.twilio.com/v1/Content/HXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Some content",
                "language": "en",
                "variables": {
                    "name": "foo"
                },
                "types": {
                    "twilio/text": {
                        "body": "Foo Bar Co is located at 39.7392, 104.9903"
                    },
                    "twilio/location": {
                        "longitude": 104.9903,
                        "latitude": 39.7392,
                        "label": "Foo Bar Co"
                    }
                },
                "url": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T19:00:00Z",
                "date_updated": "2015-07-30T19:00:00Z",
                "links": {
                    "approval_create": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests/whatsapp",
                    "approval_fetch": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests"
                }
            }
            '''
        ))

        actual = self.client.content.v1.contents("HXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.content.v1.contents("HXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://content.twilio.com/v1/Content/HXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.content.v1.contents("HXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.content.v1.contents.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://content.twilio.com/v1/Content',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "contents": [],
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://content.twilio.com/v1/Content?PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://content.twilio.com/v1/Content?PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "contents"
                }
            }
            '''
        ))

        actual = self.client.content.v1.contents.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "contents": [
                    {
                        "sid": "HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Some content",
                        "language": "en",
                        "variables": {
                            "name": "foo"
                        },
                        "types": {
                            "twilio/text": {
                                "body": "Foo Bar Co is located at 39.7392, 104.9903"
                            },
                            "twilio/location": {
                                "longitude": 104.9903,
                                "latitude": 39.7392,
                                "label": "Foo Bar Co"
                            }
                        },
                        "url": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T19:00:00Z",
                        "date_updated": "2015-07-30T19:00:00Z",
                        "links": {
                            "approval_create": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests/whatsapp",
                            "approval_fetch": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests"
                        }
                    },
                    {
                        "sid": "HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Anotha content",
                        "language": "en",
                        "variables": {
                            "name": "foo"
                        },
                        "types": {
                            "twilio/text": {
                                "body": "Foo Bar Co is located at 39.7392, 104.9903"
                            },
                            "twilio/location": {
                                "longitude": 104.9903,
                                "latitude": 39.7392,
                                "label": "Foo Bar Co"
                            }
                        },
                        "url": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T19:00:00Z",
                        "date_updated": "2015-07-30T19:00:00Z",
                        "links": {
                            "approval_create": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests/whatsapp",
                            "approval_fetch": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests"
                        }
                    },
                    {
                        "sid": "HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Third content",
                        "language": "en",
                        "variables": {
                            "name": "foo"
                        },
                        "types": {
                            "twilio/text": {
                                "body": "Foo Bar Co is located at 39.7392, 104.9903"
                            },
                            "twilio/location": {
                                "longitude": 104.9903,
                                "latitude": 39.7392,
                                "label": "Foo Bar Co"
                            }
                        },
                        "url": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T19:00:00Z",
                        "date_updated": "2015-07-30T19:00:00Z",
                        "links": {
                            "approval_create": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests/whatsapp",
                            "approval_fetch": "https://content.twilio.com/v1/Content/HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ApprovalRequests"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 20,
                    "first_page_url": "https://content.twilio.com/v1/Content?PageSize=20&Page=0",
                    "previous_page_url": null,
                    "url": "https://content.twilio.com/v1/Content?PageSize=20&Page=0",
                    "next_page_url": null,
                    "key": "contents"
                }
            }
            '''
        ))

        actual = self.client.content.v1.contents.list()

        self.assertIsNotNone(actual)
