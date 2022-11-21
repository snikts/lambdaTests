from unittest import TestCase
from WidgetRequests import WidgetRequests
import boto3
import json


class TestWidgetRequests(TestCase):
    def setUp(self):
        self.wr = WidgetRequests()
        self.sqs = boto3.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName='request-queue')

    def test_post_update(self):
        body = {
            "requestType": "update",
            "requestId": "38d51e39-c470-462b-a72b-cfd04335454e",
            "widgetId": "ad0bb9e1-28e9-46e0-ad08-8192f4d3b6c6",
            "owner": "John Jones",
            "label": "",
            "description": "QQGRLNZY",
            "otherAttributes": [
                {
                    "name": "color",
                    "value": "red"
                },
                {
                    "name": "size-unit",
                    "value": "cm"
                },
                {
                    "name": "height",
                    "value": "955"
                },
                {
                    "name": "width-unit",
                    "value": "cm"
                },
                {
                    "name": "length",
                    "value": "247"
                },
                {
                    "name": "price",
                    "value": "71.11"
                },
                {
                    "name": "vendor",
                    "value": "UPAZOD"
                },
                {
                    "name": "note",
                    "value": "MUUDBUWKGVFCXPEUSKBBBDEYQTZDNWCPPGHFBXPILELOVETUGRTWMEMZMLKUEMAEOZTSMAMNFPISAMWFYZJHDQQSOIPOGFJY"
                }
            ]
        }
        r = self.wr.post_create(body)
        r = r['ResponseMetadata']
        r = r['HTTPStatusCode']
        itemFound = False
        if(r == 202):
            itemFound = True
        self.assertEqual(itemFound, True)

    def test_post_create(self):
        body = {
            "requestType": "create",
            "requestId": "e80fab52-71a5-4a76-8c4d-11b66b83ca2a",
            "widgetId": "8123f304-f23f-440b-a6d3-80e979fa4cd6",
            "owner": "Mary Matthews",
            "label": "JWJYY",
            "description": "THBRNVNQPYAWNHGRGUKIOWCKXIVNDLWOIQTADHVEVMUAJWDONEPUEAXDITDSHJTDLCMHHSESFXSDZJCBLGIKKPUYAWKQAQI",
            "otherAttributes": [
                {
                    "name": "width-unit",
                    "value": "cm"
                },
                {
                    "name": "length-unit",
                    "value": "cm"
                },
                {
                    "name": "rating",
                    "value": "2.580677"
                },
                {
                    "name": "note",
                    "value": "FEGYXHIJCTYNUMNMGZBEIDLKXYFNHFLVDYZRNWUDQAKQSVFLPRJTTXARVEIFDOLTUSWZZWVERNWPPOEYSUFAKKAPAGUALGXNDOVPNKQQKYWWOUHGOJWKAJGUXXBXLWAKJCIVPJYRMRWMHRUVBGVILZRMESQQJRBLXISNFCXGGUFZCLYAVLRFMJFLTBOTLKQRLWXALLBINWALJEMUVPNJWWRWLTRIBIDEARTCSLZEDLZRCJGSMKUOZQUWDGLIVILTCXLFIJIULXIFGRCANQPITKQYAKTPBUJAMGYLSXMLVIOROSBSXTTRULFYPDFJSFOMCUGDOZCKEUIUMKMMIRKUEOMVLYJNJQSMVNRTNGH"
                }
            ]
        }
        r = self.wr.post_create(body)
        r = r['ResponseMetadata']
        r = r['HTTPStatusCode']
        itemFound = False
        if(r == 202):
            itemFound = True
        self.assertEqual(itemFound, True)

    def test_post_delete(self):
        body = {
            "type":"delete",
            "requestId":"21cf74b2-dbf2-46bb-a274-b8e3eac679bf",
            "widgetId":"e50b4381-4332-438f-bcec-bd2b8c0fa5ed",
            "owner":"Sue Smith"
        }
        r = self.wr.post_create(body)
        r = r['ResponseMetadata']
        r = r['HTTPStatusCode']
        itemFound = False
        if(r == 202):
            itemFound = True
        self.assertEqual(itemFound, True)
