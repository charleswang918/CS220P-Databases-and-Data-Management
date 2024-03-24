from relational_algebra import *
import sqlite3
class Expressions():

    # The following query is the solution to: Retrieve the name of all Trainers who have the credentials CNS
    sample_query = Projection(NaturalJoin(Selection(Relation("Trainer"),Equals("credentials","CNS")),Relation("person")),["name"])
    
    #expression1 = 

    #expression2 = 

    #expression3 = 

    #expression4 = 

    #expression5 =

    #expression6 = 

    #expression7 = 

    #expression8 = 

    #expression9 = 

    #expression10 = 
    
    
    sql_con = sqlite3.connect("sample220P.db")

    result = sample_query.evaluate(sql_con=sql_con)
    print(result.rows)