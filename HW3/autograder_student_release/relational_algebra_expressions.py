from relational_algebra import *
import sqlite3
class Expressions():

    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    #sample_query = Projection(NaturalJoin(Selection(Relation("Trainer"),Equals("credentials","CNS")),Relation("person")),["name"])
    
    expression1 = Projection(Relation("person"), ["name", "gender"])

    expression2 = Projection(NaturalJoin(NaturalJoin(Selection(Relation("non_student"), Equals("member_type", "Faculty")),
                              Relation("university_affiliate")), Relation("person")), ["name", "department"])

    expression3 =Projection(NaturalJoin(Selection(NaturalJoin(Relation("location_reading"), Relation("space")),
                            And(Equals("space_description", "weight room"),
                                Equals("timestamp", "2023-04-01 00:00:00"))) | Selection(NaturalJoin(Relation("location_reading"), Relation("space")),
                            And(Equals("space_description", "cardio room"),
                                Equals("timestamp", "2023-04-01 00:00:00"))),
                             Rename(Relation("person"), {"card_id": "person_id"})), ["name"])

    expression4 = Projection(NaturalJoin(Projection(Relation("attends"), ["card_id"]) - Projection(CrossProduct(Projection(Relation("attends"), ["card_id"]),
                               Projection(Relation("attends"), ["event_id"])) - Relation("attends"), ["card_id"]), Relation("person")), ["name"])

    expression5 = Projection(Selection(Projection(NaturalJoin(Relation("events"), Relation("space")),
                                       ["event_id", "capacity", "max_capacity"]), GreaterEquals("capacity", "max_capacity")),
                             ["event_id"])

    expression6 = Projection(NaturalJoin(NaturalJoin((Projection(NaturalJoin(Projection(Selection(NaturalJoin(Relation("equipment"), Relation("space")),
                                       Equals("space_description", "cardio room")), ["equipment_id"]),
                              Projection(Relation("usage_reading"), ["card_id", "equipment_id"])), ["card_id"]) -
                   Projection(((Projection(NaturalJoin(Projection(Selection(NaturalJoin(Relation("equipment"), Relation("space")),
                                       Equals("space_description", "cardio room")), ["equipment_id"]),
                              Projection(Relation("usage_reading"), ["equipment_id", "card_id"])), ["card_id"]) *
                   (Projection(NaturalJoin(Projection(Selection(NaturalJoin(Relation("equipment"), Relation("space")),
                                                Equals("space_description", "cardio room")), ["equipment_id"]),
                           Projection(Relation("usage_reading"), ["card_id", "equipment_id"])), ["equipment_id"]))) -
                   Projection(NaturalJoin(Projection(Selection(NaturalJoin(Relation("equipment"), Relation("space")),
                                       Equals("space_description", "cardio room")), ["equipment_id"]),
                              Projection(Relation("usage_reading"), ["card_id", "equipment_id"])), ["card_id", "equipment_id"])),
                             ["card_id"])), Relation("student")), Relation("person")), ["name"])

    #expression7 =

    #expression8 = 

    #expression9 = 

    #expression10 = 
    
    
    # sql_con = sqlite3.connect("sample220P.db")
    #
    # # result = sample_query.evaluate(sql_con=sql_con)
    # result = expression6.evaluate(sql_con=sql_con)
    # print(result.rows)