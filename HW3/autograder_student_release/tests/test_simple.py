import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
import sqlite3
from relational_algebra_expressions import Expressions
from relational_algebra import *

class TestRelationalAlgebraQueries(unittest.TestCase):
    def setUp(self):
        self.sqlconnection = sqlite3.connect("sample220P.db")
        self.expressions = Expressions()

    @weight(15)
    @number(1)
    def test_eval_query_one(self):
        """Retrieve the names and genders of all people associated with ARC (i.e., members, employees, etc.)"""
        result = self.expressions.expression1.evaluate(sql_con=self.sqlconnection)

        result_intermediate = {('Dr. Minerva Cormier', 'f'), ('Dr. Alexys Hand IV', 'm'), ('Hildegard Farrell', 'm'), ('Richie Hagenes Sr.', 'm'), ('Dr. Jamarcus Hamill', 'f'), ('Mustafa Bednar', 'm'), ('Eulah Reynolds DDS', 'f'), ('Prof. Marilou Stamm', 'f'), ('Tania Purdy V', 'f'), ('Mekhi Sporer', 'm'), ('Jessica Flatley', 'm'), ('Mellie Hermiston', 'f'), ('Mr. Harold Fritsch DDS', 'm'), ('Enola Hilpert', 'f'), ('Miss Elfrieda McKenzie V', 'm'), ('Mr. Stuart Ondricka IV', 'm'), ('Jacinto Quigley', 'f'), ('Coleman Wiegand', 'm'), ('Trudie Heidenreich', 'm'), ('Earlene Greenfelder', 'f'), ('Sam Bergstrom', 'm'), ('Prof. Morton Morar', 'f'), ('Prof. Hildegard Mayer V', 'f'), ('Irma Schmidt', 'f'), ('Angelita Carter', 'f'), ('Dillan Lockman', 'm'), ('Sienna Raynor', 'm'), ('Jensen Beahan', 'f'), ('Prof. Werner Torphy', 'f'), ('Ciara Brakus', 'f'), ('Damon West', 'm'), ('Leif Kohler', 'f'), ('Emilia Howe', 'm'), ('Dina McClure', 'm'), ('Antwan Stoltenberg', 'm'), ('Clay Vandervort', 'm'), ('Prof. Clarissa Zieme V', 'm'), ('Cornelius Blick', 'f'), ('Prof. Orlo Mueller', 'f'), ('Flavie Gulgowski PhD', 'f'), ('Ms. Pearl Wilkinson', 'm'), ('Juston Marks', 'f'), ('Mohammed Hilpert', 'f'), ('Dr. Kirsten Erdman', 'f'), ('Raymundo Larkin', 'm'), ('Magnus Welch', 'm'), ('Leon Nolan', 'f'), ('Zaria Hickle II', 'm'), ('Gilberto Fay', 'm'), ('Izaiah Funk V', 'f'), ('Amya Cole', 'f'), ('Dr. Jaden Miller', 'f'), ('Miss Letitia Brown', 'f'), ('Dr. Monica Anderson MD', 'f'), ('Prof. Rodrigo West V', 'f'), ('Mr. Jamir McDermott MD', 'm'), ('Prof. Rowan Cronin', 'm'), ('Jacinto Considine', 'f'), ('Ardella Casper DDS', 'm'), ('Drew Halvorson', 'm'), ('Maurine Nitzsche', 'f'), ('Colin McKenzie', 'f'), ('Dr. Loy Crooks', 'm'), ('Marlee Stanton', 'm'), ('Donny Barrows', 'f'), ('Bette Auer', 'f'), ('Mary Volkman', 'm'), ('Johnny Hodkiewicz', 'm'), ('Dina Fadel III', 'f'), ('Mr. Jovany Simonis', 'f'), ('Kody Ferry Sr.', 'f'), ('Rhea Dare', 'f'), ('Tyree Bogan', 'm'), ('Joel Wintheiser', 'f'), ('Mr. Dillan Breitenberg IV', 'f'), ('Darrion Lindgren', 'm'), ('Mariano Wilkinson', 'f'), ('Prof. Kacie Fritsch', 'f'), ('Mrs. Antonietta Flatley', 'm'), ('Brook Spencer', 'm'), ('Dr. Lilian Stark', 'f'), ('Jeanie Schaefer', 'm'), ('Terrell Maggio', 'm'), ('Elmira Daugherty II', 'f'), ('Ulises McGlynn', 'm'), ('Rosalyn Fisher', 'f'), ('Prof. Ernestine Cummerata', 'f'), ('Prudence Reinger', 'm'), ('Dr. Marc Tillman', 'f'), ('Merritt Romaguera', 'f'), ('Prof. Norbert Rath DDS', 'f'), ('Nelda Stiedemann', 'm'), ('Prof. Sylvester Williamson PhD', 'f'), ('Hildegard Legros', 'm'), ('Providenci Feeney IV', 'f'), ('Louie Bins', 'm'), ('Leonora McLaughlin', 'f'), ('Theresia Hintz', 'f'), ('Mrs. Dianna Connelly DVM', 'm'), ('Adrien Spencer', 'f')}

        try:
            self.assertEqual(result.rows, result_intermediate, "Incorrect Query")
        except:
            raise Exception("Incorrect Query")
    
    @weight(15)
    @number(2)
    def test_eval_query_two(self):
        """List the names and departments of all faculty members who are also members of ARC"""
        result = self.expressions.expression2.evaluate(sql_con=self.sqlconnection)
        result_intermediate = {('Mariano Wilkinson', 'Political Science')}
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")

    @weight(20)
    @number(3)
    def test_eval_query_three(self):

        """Find all the people who were present in either the weight room or the cardio room on 2023-04-01"""
        result = self.expressions.expression3.evaluate(sql_con = self.sqlconnection)
        
        result_intermediate = {('Mr. Stuart Ondricka IV',), ('Jacinto Quigley',)}
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")
        
        
        
    @weight(15)
    @number(4)
    def test_eval_query_four(self):
        """Find the names of people who have attended all events"""
        
        result = self.expressions.expression4.evaluate(sql_con=self.sqlconnection)
        
        result_intermediate = {('Leonora McLaughlin',)}
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")
        
        
    @weight(15)
    @number(5)
    def test_eval_query_five(self):
        """List the events whose capacity have reached the reached maximum capacity of their associated space."""
        result = self.expressions.expression5.evaluate(sql_con = self.sqlconnection)
        
        result_intermediate = {(23,)}
        
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")

    @weight(20)
    @number(6)
    def test_eval_query_six(self):
        """Find the students who have used all the equipment located in the cardio room"""

        result = self.expressions.expression6.evaluate(sql_con = self.sqlconnection)

        result_intermediate = {('Mellie Hermiston',)}

        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")
        
        
    @weight(0)
    @number(7)
    def test_eval_query_seven(self):
        """List the equipment ids and descriptions for equipment that is currently in use"""
        
        result = self.expressions.expression7.evaluate(sql_con=self.sqlconnection)
        
        result_intermediate = {(19, 'Weightlifting Gloves'), (36, 'Step Platform'), (47, 'Step Platform'), (24, 'Push-up Handles'), (23, 'Power Tower'), (46, 'Push-up Handles'), (48, 'Hex Bar'), (38, 'Grip Strengthener'), (2, 'Abdominal Mat'), (7, 'Cable Crossover'), (8, 'Resistance Loop Bands'), (18, 'Elliptical Trainer'), (43, 'Spin Bike'), (33, 'Pilates Reformer'), (22, 'Sandbags'), (29, 'Vibrating Fitness Roller'), (30, 'Bench Press'), (41, 'Balance Disc'), (39, 'Sandbags'), (28, 'Hand Grippers')}
        
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")
        
        
            
            
    @weight(0)
    @number(8)
    def test_eval_query_eight(self):
        
        """Find names of all employees in ARC"""
        result = self.expressions.expression8.evaluate(sql_con = self.sqlconnection)
        
        result_intermediate = {('Dillan Lockman',), ('Prof. Marilou Stamm',), ('Rhea Dare',), ('Nelda Stiedemann',), ('Damon West',), ('Hildegard Farrell',), ('Izaiah Funk V',), ('Darrion Lindgren',), ('Amya Cole',), ('Coleman Wiegand',), ('Angelita Carter',), ('Merritt Romaguera',), ('Ardella Casper DDS',), ('Louie Bins',), ('Prof. Rowan Cronin',), ('Dr. Lilian Stark',), ('Leif Kohler',), ('Jessica Flatley',), ('Eulah Reynolds DDS',), ('Dr. Jaden Miller',)}
        
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")
        
    @weight(0)
    @number(9)
    def test_eval_query_nine(self):
        """Retrieve the names of all members who have attended an event in the yoga studio"""

        result = self.expressions.expression9.evaluate(sql_con=self.sqlconnection)

        result_intermediate = {('Adrien Spencer',), ('Dr. Alexys Hand IV',), ('Maurine Nitzsche',), ('Flavie Gulgowski PhD',), ('Mrs. Dianna Connelly DVM',), ('Leonora McLaughlin',), ('Prof. Norbert Rath DDS',), ('Prof. Morton Morar',), ('Drew Halvorson',), ('Rosalyn Fisher',), ('Mary Volkman',), ('Terrell Maggio',), ('Prof. Werner Torphy',), ('Sienna Raynor',)}
        
        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")
        
        
    @weight(0)
    @number(10)
    def test_eval_query_ten(self):
        
        """Find all family members who have attended Summer Splash Fest"""
        result = self.expressions.expression10.evaluate(sql_con = self.sqlconnection)
        
        result_intermediate = {('Ulises McGlynn',), ('Mary Volkman',)}

        try:
            self.assertEqual(result.rows,result_intermediate,"Incorrect Query")
        except:
            raise Exception("Incorrect Query")

