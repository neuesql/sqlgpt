from unittest import TestCase, skip
import os

import loguru
import openai
import SQLTransformer


class TestSQLTransformer(TestCase):

    def setUp(self) -> None:
        self.client = SQLTransformer(os.getenv("OPENAPI_KEY"), os.getenv("OPENAPI_SECRET"))

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
