import contextlib
import json

from models import Claimant, Employer, Employee
from base import make_session



def add_rp1_form(dictionary):
    with contextlib.closing(make_session()) as session:
        claimant = Claimant()
        claimant.nino = dictionary["nino"]
        claimant.date_of_birth = dictionary["date_of_birth"]
        claimant.title = dictionary["title"]
        claimant.forenames = dictionary["forenames"]
        claimant.surname = dictionary["surname"]
        claimant.hstore = {key: json.dumps(value)
                           for key, value in dictionary.items()}
        session.add(claimant)
        session.commit()


def add_rp14_form(dictionary):
    with contextlib.closing(make_session()) as session:
        employer = Employer()
        employer.ip_number = dictionary["ip_number"]
        employer.employer_name = dictionary["employer_name"]
        employer.company_number = dictionary["company_number"]
        employer.date_of_insolvency = dictionary["date_of_insolvency"]
        employer.hstore = {key: json.dumps(value)
                           for key, value in dictionary.items()}
        session.add(employer)
        session.commit()


def add_rp14a_form(dictionary):
    with contextlib.closing(make_session()) as session:
        employee = Employee()
        employee.nino = dictionary["nino"]
        employee.date_of_birth = dictionary["date_of_birth"]
        employee.title = dictionary["title"]
        employee.forenames = dictionary["forenames"]
        employee.surname = dictionary["surname"]
        employee.ip_number = dictionary["ip_number"]
        employee.employer_name = dictionary["employer_name"]
        employee.hstore = {key: json.dumps(value)
                           for key, value in dictionary.items()}
        session.add(employee)
        session.commit()
