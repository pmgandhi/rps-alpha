from base import Base

from sqlalchemy import(
    Column,
    Integer,
    Text,
    Date,
    ForeignKey
    )
from sqlalchemy.dialects.postgresql import HSTORE

class Claimant(Base):
    __tablename__ = 'claimants'

    claimant_id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    forenames = Column(Text, nullable=False)
    surname  = Column(Text, nullable=False)
    nino = Column(Text) # nullable?
    date_of_birth = Column(Date, nullable=False)
    hstore = Column(HSTORE)


class Employer(Base):
    __tablename__ = "employers"

    employer_id = Column(Integer, primary_key=True)
    ip_number = Column(Text, nullable=False)
    employer_name  = Column(Text, nullable=False)
    company_number  = Column(Text, unique=True, index=True, nullable=False)
    date_of_insolvency  = Column(Date, nullable=False)
    hstore = Column(HSTORE)


class InsolvencyPractitioner(Base):
    __tablename__ = "insolvency_practitioners"

    ip_id = Column(Integer, primary_key=True)
    name  = Column(Text, nullable=False)
    registration_number  = Column(Text, nullable=False)
    insolvency_practitioner_firm  = Column(Text, nullable=False) # FK?
    hstore = Column(HSTORE)