import unittest

from birmingham_cabinet.base import make_session, Base
from birmingham_cabinet.models import Claimant

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.session = make_session()

    def tearDown(self):
        self.session.query(Claimant).delete()
        self.session.commit()
        self.session.close()

    def test_should_be_able_to_save_a_claimant(self):
        claimant = Claimant()
        claimant.claimant_id = 1000
        self.session.add(claimant)
        self.session.commit()

        found = self.session.query(Claimant).filter(
            Claimant.claimant_id == 1000).count()
        self.assertEqual(found, 1)
