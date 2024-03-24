import mysql.connector
from constants import Constants

class Queries(object):
    """Database queries"""
    # connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, database=Constants.DATABASE)
    # cursor = connection.cursor()

    """Retrieve the names and genders of all people associated with ARC (i.e., members, employees, etc.)"""
    
    query1 = "select name, gender from person;"
    
    query2 = ("select name, department from non_student natural join person natural join university_affiliate "
              "where member_type = \"Faculty\";")
    
    query3 = ("with cte as(select * from location_reading natural join space "
              "where description in (\"weight room\", \"cardio room\") and timestamp = \"2023-04-01 00:00:00\") "
              "select distinct name from cte join person on cte.person_id = person.card_id;")
    
    query4 = ("select name from "
              "(with cte as (select * from ((select card_id from person) as p cross join (select event_id from events) as e)) "
              "select distinct card_id from events natural join attends "
              "where card_id not in (select cte.card_id from cte where (card_id, event_id) not in (select card_id, event_id from events natural join attends))) as p1 natural join person;")

    query5 = ("select events.event_id from events join space on events.space_id = space.space_id "
              "where events.capacity >= space.max_capacity;")

    query6 = ("with cte as "
              "(select card_id, equipment_id from student natural join usage_reading "
              "where equipment_id in (select equipment_id from equipment where space_id = "
              "(select space_id from space where description = \"cardio room\"))), "
              "cte2 as(select * from ((select card_id from cte) as p cross join (select equipment_id from cte) as e) "
              "where (card_id, equipment_id) not in (select card_id, equipment_id from cte)) "
              "select distinct name from cte natural join person where card_id not in (select card_id from cte2);")

    query7 = "select equipment_id, equipment_type from equipment where is_available = 1;"
    
    query8 = "select name from employee natural join person;"
    
    query9 = ("select distinct name from events natural join attends natural join person "
              "where space_id = (select space_id from space where description = \"yoga studio\");")
    
    query10 = ("select name from attends natural join family natural join person "
               "where event_id = (select event_id from events where description = \"Summer Splash Fest\")")

    query11 = "select avg(salary_hour) from employee where employee_type = \"student\";"

    query12 = ("with cte as "
               "(select person_id, salary_hour from Trainer join employee on Trainer.person_id = employee.card_id) "
               "select name from cte join person on cte.person_id = person.card_id "
               "where salary_hour in (select max(salary_hour) from cte where salary_hour < (select max(salary_hour) from cte));")

    query13 = ("select count(*) from location_reading natural join space "
               "where description = \"weight room\" and person_id = (select card_id from person where name = \"Mekhi Sporer\");")

    query14 = ("with counts as "
               "(select count(*) nod, person_id, name from location_reading natural join space "
               "join person on person_id = person.card_id join member on person_id = member.card_id "
               "where timestamp like (\"2023-05%\") and description = \"cardio room\" group by person_id) "
               "select name from counts where nod = (select max(nod) from counts);")

    query15 = ("with cte as"
               "(select count(card_id) as counts, event_id from attends as counts group by event_id), "
               "cte2 as(select space_id, sum(counts)/count(events.event_id) as avg_occupancy from cte join events on cte.event_id = events.event_id group by space_id) "
               "select description, avg_occupancy from cte2 natural join space where avg_occupancy = (select min(avg_occupancy) from cte2)")
    
    # cursor.execute(query15)
    #
    # print(cursor.fetchall())
