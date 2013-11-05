import unittest

from birmingham_cabinet.base import make_session
from birmingham_cabinet.models import Claimant

class TestDatabase(unittest.TestCase):
	def setUp(self):
		self.session = make_session()
		
	def tearDown(self):
		self.session.close()
		
	@unittest.expectedFailure
	def test_should_be_able_to_save_a_claimant(self):
		self.session.add(Claimant())
		self.session.commit()