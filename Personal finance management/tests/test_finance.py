import unittest
import sqlite3
from db import init_db

class TestFinance(unittest.TestCase):
    def setUp(self):
        init_db()
        self.conn = sqlite3.connect("finance.db")
        self.cursor = self.conn.cursor()

    def test_user_table_exists(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNotNone(self.cursor.fetchone())

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
