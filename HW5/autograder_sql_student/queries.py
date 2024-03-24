class Queries(object):
    """Database queries"""

    query1 = ("create view Top_Machines_Used as select equipment_type as \"Equipment Name\", count(distinct timestamp) as \"Total Number of Days Used\", "
              "count(distinct card_id) as \"Number Of Unique Users Using Equipment\", rank() over (order by count(distinct card_id) desc) as \"Rank\" from usage_reading natural join equipment "
              "where timestamp between \"2023-01-01\" and \"2023-06-30\" group by equipment_type limit 15;")

    query2 = ("create view Machines_Used_By_Day_Of_Week as with cte as("
              "select equipment_type, CASE DAYOFWEEK(timestamp) "
              "WHEN 1 THEN 'Sunday' WHEN 2 THEN 'Monday' WHEN 3 THEN 'Tuesday' WHEN 4 THEN 'Wednesday' WHEN 5 THEN 'Thursday' WHEN 6 THEN 'Friday' WHEN 7 THEN 'Saturday' "
              "END AS DayOfWeek, CASE WHEN card_id in (select card_id from family) THEN 'Family' "
              "WHEN card_id in (select card_id from student) THEN (select student_type from student where student.card_id = usage_reading.card_id) "
              "WHEN card_id in (select card_id from non_student) THEN (select member_type from non_student where non_student.card_id = usage_reading.card_id) "
              "END AS TypeOfMember, count(*) as Count from usage_reading natural join equipment group by equipment_type, TypeOfMember, DayOfWeek with rollup)"
              "select equipment_type as \"Equipment Name\", DayOfWeek as \"Day Of Week\", TypeOfMember as \"Type Of Member\", Count from cte limit 678;")

    query3 = "CREATE TRIGGER NoLowerSalary BEFORE UPDATE ON employee FOR EACH ROW BEGIN IF NEW.salary_hour < OLD.salary_hour THEN SET NEW.salary_hour = OLD.salary_hour; END IF; END;"

    query4 = "ALTER TABLE employee ADD constraint chk_salary_range CHECK (employee.salary_hour >= 12);"

    query5 = ("with recursive rec_supervisor(card_id, supervisor_card_id) as (select card_id, supervisor_card_id from employee "
              "union select rec_supervisor.card_id, employee.supervisor_card_id from rec_supervisor join employee on rec_supervisor.supervisor_card_id = employee.card_id), "
              "cte as (select card_id, count(*) as length from rec_supervisor group by card_id) select max(length) from cte;")

    query6 = ("with cte as (select name, salary_hour, dob, dense_rank() over (order by dob desc) as ranking from person natural join employee "
              "where salary_hour = (select max(salary_hour) from employee)) select name from cte where ranking = 2;")
