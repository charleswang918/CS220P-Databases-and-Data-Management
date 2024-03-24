# CS220P Assignment 4
use cs220p;
show tables;
#1 Retrieve the names and genders of all people associated with ARC (i.e., members, employees, etc.)
select name, gender from person;

#2 List the names and departments of all ‘Faculty’ members who are also members of ARC. 
select name, department from non_student natural join person natural join university_affiliate
where member_type = "Faculty";

#3 Find the names of the people who were present in either the ‘weight room’ or the ‘cardio room’ on 2023-04-01.
with cte as(select * from location_reading natural join space
where description in ("weight room", "cardio room") and timestamp = "2023-04-01 00:00:00")
select distinct name from cte join person on cte.person_id = person.card_id;

#4 Find the names of the people who have attended all events. 
select name from (with cte as (
select * from ((select card_id from person) as p cross join (select event_id from events) as e)
)
select distinct card_id from events natural join attends
where card_id not in (
select cte.card_id from cte where (card_id, event_id) not in (select card_id, event_id from events natural join attends)
)
) as p1 natural join person;

#5 List the events whose capacity have reached the maximum capacity of their associated space. (Just project the event ids)
select events.event_id from events join space on events.space_id = space.space_id
where events.capacity >= space.max_capacity;

#6 Find the names of students who have used all the equipment located in the cardio room. 
with cte as (
select card_id, equipment_id from student natural join usage_reading
where equipment_id in (
select equipment_id from equipment
where space_id = (
select space_id from space where description = "cardio room"
))),
cte2 as(
select * from ((select card_id from cte) as p cross join (select equipment_id from cte) as e)
where (card_id, equipment_id) not in (select card_id, equipment_id from cte)
)
select distinct name from cte natural join person where card_id not in (select card_id from cte2);

#7 List the equipment ids and types for equipment that is currently in use. (1 for in use)
select equipment_id, equipment_type from equipment
where is_available = 1;

#8 Find names of all employees in ARC. 
select name from employee natural join person;

#9 Retrieve the names of all members who have attended an event in the yoga studio. 
select distinct name from events natural join attends natural join person where space_id = (
select space_id from space where description = "yoga studio"
);

#10  Find all family members who have attended ‘Summer Splash Fest’. 
select name from attends natural join family natural join person 
where event_id = (select event_id from events where description = "Summer Splash Fest");

#11 Calculate the average hourly rate paid to all employees who are of student type  at ARC
select avg(salary_hour) from employee where employee_type = "student";

#12 Find the trainer(s) with the 2nd highest average hourly rate
with cte as (
select person_id, salary_hour from Trainer join employee on Trainer.person_id = employee.card_id
)
select name from cte join person on cte.person_id = person.card_id where salary_hour = (
select max(salary_hour) from cte
where salary_hour < (select max(salary_hour) from cte)
);


#13 Calculate the total duration spent by Mekhi Sporer in the weight room. (count the number of days they have visited the weight room)
select count(*) from location_reading natural join space
where description = "weight room" and person_id = (select card_id from person where name = "Mekhi Sporer");

#14 Find the names of the member(s) who spent the most time in the cardio room in the month of May. (count the number of days they have visited the cardio room)
with counts as (select count(*) nod, person_id, name from location_reading 
natural join space join person on person_id = person.card_id join member on person_id = member.card_id
where timestamp like ("2023-05%") and description = "cardio room"
group by person_id)
select name from counts
where nod = (select max(nod) from counts);

#15  Find the name and the average occupancy of the space which has the lowest average occupancy per event. ( you need to get the occupancy from the attends table.
with cte as(
select count(card_id) as counts, event_id from attends as counts group by event_id
),
cte2 as(
select space_id, sum(counts)/count(events.event_id) as avg_occupancy from cte join events on cte.event_id = events.event_id group by space_id
)
select description, avg_occupancy from cte2 natural join space where avg_occupancy = (select min(avg_occupancy) from cte2)

