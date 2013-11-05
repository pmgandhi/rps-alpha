from base import Base

from sqlalchemy import(
    Column,
    Integer,
    Text,
    Date,
    ForeignKey
    )

class Claimant(Base):
    __tablename__ = 'claimants'

    claimant_id = Column(Integer, primary_key=True)

class Employer(Base):
    __tablename__ = "employers"

    employer_id = Column(Integer, primary_key=True)
    employer_name  = Column(Text, nullable=False)
    company_number  = Column(Text, unique=True, index=True, nullable=False)
    nature_of_business  = Column(Text, nullable=False) # possibly an FK?
    address_line_1  = Column(Text, nullable=False)
    address_line_2  = Column(Text, nullable=False)
    address_line_3  = Column(Text, nullable=False)
    town_or_city  = Column(Text, nullable=False)
    postcode  = Column(Text, nullable=False)
    country  = Column(Text, nullable=False) # FIXME: Should be an FK
    email_address  = Column(Text, nullable=False)
    telephone_number  = Column(Text, nullable=False)
    date_of_insolvency  = Column(Date, nullable=False)
    type_of_insolvency  = Column(Text, nullable=False) # FIXME: Should be an FK

class InsolvencyPractitionerEmployer(Base):
    __tablename__ = "insolvency_practitioner_employer"

    employer_id = Column(Integer,
        ForeignKey("employers.employer_id"), primary_key=True)
    insolvency_practitioner_id = Column(Integer,
        ForeignKey("insolvency_practitioners.ip_id"), primary_key=True)


class InsolvencyPractitioner(Base):
    __tablename__ = "insolvency_practitioners"

    ip_id = Column(Integer, primary_key=True)
    name  = Column(Text, nullable=False)
    registration_number  = Column(Text, nullable=False)
    insolvency_practitioner_firm  = Column(Text, nullable=False) # FK?
