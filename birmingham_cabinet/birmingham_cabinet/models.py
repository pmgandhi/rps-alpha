from base import Base

from sqlalchemy import(
	Column,
	Integer
	)

class Claimant(Base):
	__tablename__ = 'claimants'

	claimant_id = Column(Integer, primary_key=True)
