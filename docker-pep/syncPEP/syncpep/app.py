from ast import Assign
from sqlmodel import Session, select
import datetime

from database import create_db_and_tables, engine, write_to_db, delete_db_file
from model import Assignments, CalenderDays, Duties, Employes, Missions


def write_calender_days(year: int) -> None:
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 2, 1)
    current_date = CalenderDays(date=start_date)

    days = []
    while current_date.date <= end_date:
        days.append(current_date)
        current_date = CalenderDays(date=current_date.date + datetime.timedelta(days=1))

    write_to_db(days)


def write_sample_data() -> None:
    duty_onCall = Duties(abbr="RB")
    duty_at = Duties(abbr="AT")
    duty_we = Duties(abbr="WE")
    duty_ko = Duties(abbr="KO")
    duty_ca = Duties(abbr="CA")
    duty_de = Duties(abbr="DE")
    duty_sick = Duties(abbr="k")
    duty_edu = Duties(abbr="L")
    duties = [
        duty_at,
        duty_ca,
        duty_de,
        duty_onCall,
        duty_ko,
        duty_we,
        duty_sick,
        duty_edu,
    ]

    e1 = Employes(surnameName="Mustermann", firstname="Max", positionID="N32AT66")
    e2 = Employes(surnameName="Gomez", firstname="Jose", positionID="N32AT67")


    m1 = Missions(startDate=datetime.date(2024,1,2), endDate=datetime.date(2024,1,5), duty=duty_ko.id)
    m2 = Missions(startDate=datetime.date(2024,1,7), endDate=datetime.date(2024,1,8), duty=duty_ko.id)
    m3 = Missions(startDate=datetime.date(2024,1,10), endDate=datetime.date(2024,1,15), duty=duty_ko.id)
    m4 = Missions(startDate=datetime.date(2024,1,20), endDate=datetime.date(2024,1,20), duty=duty_ko.id)

    a1 = Assignments(employe=)
    write_to_db(duties)
    write_to_db([e1, e2])
    write_to_db([m1,m2])





def main() -> None:
    delete_db_file()

    create_db_and_tables()
    write_calender_days(year=2024)
    write_sample_data()


if __name__ == "__main__":
    main()
