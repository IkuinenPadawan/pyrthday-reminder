CREATE DATABASE birthdays;

-- connect to the newly created database
\c birthdays

CREATE TABLE Persons (
    person_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    birthday DATE
);

INSERT INTO Persons (first_name, birthday)
VALUES
('Teddy', TO_DATE('1858-01-06', 'YYYY-MM-DD')),
