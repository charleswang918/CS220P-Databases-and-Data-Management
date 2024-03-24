drop database if exists sampleMDSDB;

create database sampleMDSDB;
use sampleMDSDB;

CREATE TABLE Patients (
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (name)
);

CREATE TABLE RecoveredPatients (
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (name)
);

CREATE TABLE Diagnosis (
  pname VARCHAR(255) NOT NULL,
  disease VARCHAR(255) NOT NULL,
  diagnosis_date DATE NOT NULL,
  FOREIGN KEY (pname) REFERENCES Patients(name)
);

CREATE TABLE ToDiagnose (
  disease VARCHAR(255) NOT NULL,
  test VARCHAR(255) NOT NULL,
  PRIMARY KEY (disease, test)
);

CREATE INDEX Outcomes_ibfk_2_idx ON ToDiagnose (test);


CREATE TABLE Outcomes (
  pname VARCHAR(255) NOT NULL,
  test VARCHAR(255) NOT NULL,
  result VARCHAR(255) NOT NULL,
  test_date DATE NOT NULL,
  FOREIGN KEY (test) REFERENCES ToDiagnose(test)
);


-- Insert the data into the tables
INSERT INTO Patients (name, age) VALUES ('Mary', 45), ('Jane', 60), ('Mehdi', 33), ('Alex', 30), ('Bob', 27), ('John', 60), ('Al', 33), ('Barbara', 30);

INSERT INTO RecoveredPatients (name, age) VALUES ('Mary', 45), ('John', 60), ('Al', 33), ('Barbara', 30), ('Alex', 27);

INSERT INTO Diagnosis (pname, disease, diagnosis_date) VALUES ('Mary', 'Flu', '2021-01-01'), ('Jane', 'COVID', '2021-01-01'), ('Mehdi', 'Mono', '2021-01-02'), ('Alex', 'Strep', '2021-01-03'), ('Bob', 'Mono', '2021-02-01'), ('John', 'COVID', '2021-02-10'), ('Al', 'Strep', '2021-02-16'), ('Mary', 'Strep', '2021-02-16'), ('Mehdi', 'Meningitis', '2021-02-10');

INSERT INTO ToDiagnose (disease, test) VALUES ('Flu', 'A'), ('COVID', 'B'), ('Mono', 'C'), ('Strep', 'D'), ('Mono', 'E'), ('COVID', 'F'), ('Strep', 'G'), ('Meningitis', 'H');

INSERT INTO Outcomes (pname, test, result, test_date) VALUES ('Mary', 'A', 'true', '2021-01-01'), ('Mary', 'B', 'false', '2021-01-01'), ('Mary', 'D', 'true', '2021-01-01'), ('Jane', 'B', 'true', '2021-01-01'), ('Jane', 'C', 'false', '2021-01-01'), ('Jane', 'F', 'false', '2021-01-01'), ('Mehdi', 'E', 'true', '2021-01-02'), ('Mehdi', 'E', 'false', '2021-01-02'), ('Mehdi', 'F', 'true', '2021-01-02'), ('Alex', 'G', 'true', '2020-01-03'), ('Bob', 'C', 'true', '2021-02-01'), ('Al', 'G', 'true', '2020-02-16'), ('Barbara', 'G', 'false', '2020-02-10'), ('Alex', 'A', 'true', '2020-01-03'), ('Mary', 'A', 'true', '2020-01-01');
