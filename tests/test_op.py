from unittest import TestCase

import sqlalchemy
from testcontainers.postgres import PostgresContainer
from testcontainers.oracle import OracleDbContainer


class TestOraclePostgresql(TestCase):

    def setUp(self) -> None:
        self.pgdb = PostgresContainer("postgres:15")
        self.pgdb.start()

        self.oracledb = OracleDbContainer("wnameless/oracle-xe-11g-r2")
        self.oracledb.start()

    def tearDown(self) -> None:
        self.pgdb.stop()

    def test_pg_version(self):
        pge = sqlalchemy.create_engine(self.pgdb.get_connection_url())
        pre = pge.execute("select version()")
        self.assertIsNotNone(pre)

    def test_oracle_version(self):
        oe = sqlalchemy.create_engine(self.oracledb.get_connection_url())
        pe = oe.execute("select version()")
        self.assertIsNotNone(pe)
