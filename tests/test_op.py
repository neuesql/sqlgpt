from unittest import TestCase, skip

import sqlalchemy
from testcontainers.postgres import PostgresContainer
from testcontainers.oracle import OracleDbContainer
# import os
# os.environ["DOCKER_HOST"] = 'tcp://127.0.0.1:2375'

class TestOraclePostgresql(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.pgdb = PostgresContainer("postgres:15")
        cls.pgdb.start()

        # cls.oracledb = OracleDbContainer("wnameless/oracle-xe-11g-r2")
        # cls.oracledb.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.pgdb.stop()
        # cls.oracledb.stop()

    def test_pg_version(self):
        pge = sqlalchemy.create_engine(self.pgdb.get_connection_url())
        pre = pge.execute("select version()")
        print(pre)
        self.assertIsNotNone(pre)

    # @skip
    # def test_oracle_version(self):
    #     oe = sqlalchemy.create_engine(self.oracledb.get_connection_url())
    #     pe = oe.execute("select version()")
    #     print(pe)
    #     self.assertIsNotNone(pe)
