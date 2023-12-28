CREATE TABLE Employees (
    Emp_Id INT PRIMARY KEY,
    Emp_Name VARCHAR(50),
    Dept_Id INT,
    FOREIGN KEY (Dept_Id) REFERENCES Departments(Dept_Id)
);

-- To insert data into Employess dept
INSERT INTO Employees (Emp_Id, Emp_Name, Dept_Id) VALUES
(1, 'Ramesh Bag', 1),  
(2, 'Rahul Parajuli', 2); 

-- To see data in Employees table 
select *from Employees;

CREATE TABLE Departments (
    Dept_Id INT PRIMARY KEY,
    Dept_Name VARCHAR(50)
);
-- To see tables on database
show tables;

-- insert data into Departments

INSERT INTO Departments (Dept_Id, Dept_Name) VALUES
(1, 'IT'),
(2, 'HR');

-- To see data into Departments table

select *from Departments;


CREATE TABLE Marketing (
    Emp_Id INT PRIMARY KEY,
    Emp_Name VARCHAR(50),
    Dept_Id INT,
    FOREIGN KEY (Dept_Id) REFERENCES Departments(Dept_Id)
);

show tables;

-- insert data into Maeketing table
INSERT INTO Marketing (Emp_Id, Emp_Name, Dept_Id) VALUES
(1, ' Rita Thapa', 1), 
(3, 'Max Bahadur', 2);

-- select *from Marketing
-- Canteen Table
CREATE TABLE Canteen (
    Emp_ID INT PRIMARY KEY NOT NULL,
    Emp_Name VARCHAR(50)
);
-- Insert data into Canteen Table

-- Inserting individual records into the Canteen table
INSERT INTO Canteen (Emp_ID, Emp_Name) VALUES
(100, 'Rita'),
(101, 'Sita'),
(102, 'Bikash');


-- Salary Table 


CREATE TABLE Salary (
    Salary_Id INT PRIMARY KEY,
    Employee_Id INT,
    Marketing_Id INT,
    Amount DECIMAL(10, 2),

    FOREIGN KEY (Employee_Id) REFERENCES Employees(Emp_Id),
    FOREIGN KEY (Marketing_Id) REFERENCES Marketing(Emp_Id)
);
show tables;

-- Assign salaries to Employees from the Employees table
INSERT INTO Salary (Salary_Id, Employee_Id, Amount)
VALUES
(1, 1, 5000.00),  
(2, 2, 4800.00);  

-- Assign salaries to Marketing employees from the Marketing table
INSERT INTO Salary (Salary_Id, Marketing_Id, Amount)
VALUES
(3, 1, 5500.00), 
(4, 3, 5200.00);  
select*from Salary;















