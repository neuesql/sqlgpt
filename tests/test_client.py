from unittest import TestCase, skip
import os

import loguru
import openai

from src.client import SQLTransformer


class TestSQLTransformer(TestCase):

    def setUp(self) -> None:
        org = 'org-LApth0Z5jom3MtfJQflCxXk6'
        key = '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'
        self.client = SQLTransformer(org, key)

    def test_ping(self):
        ms = openai.Model.list()
        print(ms.data)
        self.assertIsNotNone(ms)

    def test_generate(self):
        source = 'oracle'
        target = 'postgresql'
        sql = "SELECT ID, CLIENT_ID FROM CUSTOMER WHERE ROWNUM <= 100 ORDER BY CREATE_TIME DESC;"
        choices = self.client.generate(source, target, sql)
        self.assertGreaterEqual(1, len(choices))
